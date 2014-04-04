package jenkins.plugins.installshield;

import hudson.Extension;
import hudson.tasks.Builder;
import org.kohsuke.stapler.DataBoundConstructor;

import jenkins.python.expoint.BuilderPW;
import jenkins.python.descriptor.BuildStepDescriptorPW;

public class InstallShieldBuilder extends BuilderPW {

    public final String builderVersion;
    public final String projectFile;
    public final String cmdArgs;

    @DataBoundConstructor
    public InstallShieldBuilder(String builderVersion, String projectFile, String cmdArgs) {
        this.builderVersion = builderVersion;
        this.projectFile = projectFile;
        this.cmdArgs = cmdArgs;
    }

    @Extension
    public static final class ISBuilderDescr extends BuildStepDescriptorPW<Builder> {
        
    }
}
