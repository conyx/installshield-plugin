package jenkins.plugins.installshield;

import hudson.Extension;
import hudson.util.FormValidation;
import hudson.tasks.Builder;
import org.kohsuke.stapler.DataBoundConstructor;
import org.kohsuke.stapler.QueryParameter;

import jenkins.python.expoint.BuilderPW;
import jenkins.python.descriptor.BuildStepDescriptorPW;

public class InstallShieldBuilder extends BuilderPW {

    private final String name;

    @DataBoundConstructor
    public InstallShieldBuilder(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Extension
    public static final class DescriptorImpl extends BuildStepDescriptorPW<Builder> {

        public DescriptorImpl() {
            execPython("descriptor_impl");
        }

        private boolean useFrench;

        public boolean getUseFrench() {
            return useFrench;
        }
        
        public void setUseFrench(boolean french) {
            useFrench = french;
        }
        
        public FormValidation doCheckName(@QueryParameter String value) {
            return (FormValidation)execPython("do_check_name", value);
        }
    }
}
