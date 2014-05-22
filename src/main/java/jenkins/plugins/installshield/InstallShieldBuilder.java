package jenkins.plugins.installshield;

import hudson.Extension;
import hudson.tasks.Builder;
import org.kohsuke.stapler.DataBoundConstructor;

import jenkins.python.expoint.BuilderPW;
import jenkins.python.descriptor.BuildStepDescriptorPW;

public class InstallShieldBuilder extends BuilderPW {

    public String builderVersion;
    public String projectFile;
    public String cmdArgs;

    @DataBoundConstructor
    public InstallShieldBuilder(String builderVersion, String projectFile, String cmdArgs) {
        execPython("install_shield_builder", builderVersion, projectFile, cmdArgs);
    }

    @Extension
    public static final class ISBuilderDescr extends BuildStepDescriptorPW<Builder> {
        
    }
}
