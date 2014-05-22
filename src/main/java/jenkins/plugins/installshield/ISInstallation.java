package jenkins.plugins.installshield;

import hudson.EnvVars;
import hudson.Extension;
import hudson.model.EnvironmentSpecific;
import hudson.model.Node;
import hudson.model.TaskListener;
import hudson.slaves.NodeSpecific;
import org.kohsuke.stapler.DataBoundConstructor;

import jenkins.python.expoint.ToolInstallationPW;
import jenkins.python.descriptor.ToolDescriptorPW;

import java.io.IOException;

public final class ISInstallation extends ToolInstallationPW implements NodeSpecific<ISInstallation>, EnvironmentSpecific<ISInstallation> {

    @DataBoundConstructor
    public ISInstallation(String name, String home) {
        super(name, home, null);
    }

    public ISInstallation forNode(Node node, TaskListener log) throws IOException, InterruptedException {
        return (ISInstallation)execPython("for_node", node, log);
    }

    public ISInstallation forEnvironment(EnvVars environment) {
        return (ISInstallation)execPython("for_environment", environment);
    }

    @Extension
    public static class ISInstallationDescr extends ToolDescriptorPW<ISInstallation> {
        public ISInstallationDescr() {
            execPython("is_installation_descr");
        }
    }
}
