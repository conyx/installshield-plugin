#!/usr/bin/env jython

import subprocess

import hudson.model.Computer as Computer
import hudson.Util as Util
import jenkins.model.Jenkins as Jenkins

def install_shield_builder(version, project_file, cmd_args):
    extension.builderVersion = version
    extension.projectFile = project_file
    extension.cmdArgs = cmd_args

def find_project_file(build):
    module_root = build.getModuleRoot().list().toArray().tolist()
    workspace = build.getWorkspace().list().toArray().tolist()
    for child in module_root + workspace:
        file_name = child.getName()
        if file_name.endswith(".ism") or file_name.endswith(".ise"):
            return file_name
    return "__undefined__"

def perform(build, launcher, listener):
    logger = listener.getLogger()
    jenkins = Jenkins.getInstance()
    node = Computer.currentComputer().getNode()
    env = build.getEnvironment(listener)
    command = ""
    # get a InstallShield version name for this task/project
    is_builder_version = extension.builderVersion
    if is_builder_version == None or is_builder_version.strip() == "":
        listener.fatalError("InstallShield builder version for this project " +
                            "is not specified!")
        return False
    isi_descr_name = "jenkins.plugins.installshield.ISInstallation"
    isi_descr = jenkins.getDescriptorByName(isi_descr_name)
    # get global InstallShield installations list
    installations = isi_descr.getInstallations()
    if installations == None:
        listener.fatalError("InstallShield builder versions are not set " +
                            "(see global options)!")
        return False
    # choose the correct installation from the list
    is_installation = None
    for installation in installations.tolist():
        if is_builder_version == installation.getName():
            is_installation = installation
            break
    if is_installation == None:
        listener.fatalError("InstallShield builder version " +
                            is_builder_version + " cannot be found!")
        return False
    # translate the installation for the environment and the node
    is_installation = is_installation.forNode(node, listener)
    is_installation = is_installation.forEnvironment(env)
    # get path to the ISCmdBld.exe executable
    is_builder_path = is_installation.getHome()
    command += '"' + is_builder_path + '"'
    # add -p "projectfile.ism"
    project_file = extension.projectFile.strip()
    if project_file != "":
        project_file = Util.replaceMacro(project_file, env)
        project_file = Util.replaceMacro(project_file, build.getBuildVariables())
    else:
        project_file = find_project_file(build)
    if build.getModuleRoot().child(project_file).exists():
        project_file_path = build.getModuleRoot().child(project_file)
    elif build.getWorkspace().child(project_file).exists():
        project_file_path = build.getWorkspace().child(project_file)
    else:
        listener.fatalError("Project file " + project_file +
                            " cannot be found in the workspace!")
        return False
    command += ' -p "' + project_file_path.toString() + '"'
    # add other command line arguments
    arguments = extension.cmdArgs.strip()
    arguments = Util.replaceMacro(arguments, env)
    arguments = Util.replaceMacro(arguments, build.getBuildVariables())
    command += ' ' + arguments
    # launch InstallShield builder (ISCmdBld.exe)
    logger.println("Executing command: " + command)
    popen = subprocess.Popen(command, shell=False,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = popen.communicate()
    for line in stdoutdata.splitlines():
        logger.println(line)
    for line in stderrdata.splitlines():
        logger.println(line)
    logger.println("ISCmdBld.exe ERRORLEVEL code: " + str(popen.returncode))
    if popen.returncode == 0:
        return True
    else:
        return False
