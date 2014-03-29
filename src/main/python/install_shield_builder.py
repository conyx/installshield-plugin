#!/usr/bin/env jython

import os
import subprocess

import hudson.Util as Util
import jenkins.model.Jenkins as Jenkins

def perform(build, launcher, listener):
    logger = listener.getLogger()
    jenkins = Jenkins.getInstance()
    command = ""
    # get InstallShield version name for this task
    is_builder_version = extension.builderVersion
    if is_builder_version == None or is_builder_version.strip() == "":
        listener.fatalError("InstallShield builder version for this project " +
                            "is not specified!");
        return False
    isi_descr_name = "jenkins.plugins.installshield.ISInstallation"
    isi_descr = jenkins.getDescriptorByName(isi_descr_name)
    # get global InstallShield installations list
    installations = isi_descr.getInstallations()
    if installations == None:
        listener.fatalError("InstallShield builder versions are not set " +
                            "(see global options)!");
        return False
    # choose correct ISCmdBld.exe version and its path from the list
    is_builder_path = None
    for installation in installations.tolist():
        if is_builder_version == installation.getName():
            is_builder_path = installation.getHome()
            break
    if is_builder_path == None:
        listener.fatalError("InstallShield builder version " +
                            is_builder_version + " cannot be found!");
        return False
    ### TODO
    command += '"' + is_builder_path + '"'
    # add -p "projectfile.ism"
    project_file = extension.projectFile
    ### TODO
    # add other command line arguments
    ### TODO
    # launch InstallShield builder
    logger.println("Executing command: " + command)
    popen = subprocess.Popen(command, shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = popen.communicate()
    status = popen.returncode
    ### TODO
    # return result
    ### TODO
    return True
