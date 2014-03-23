#!/usr/bin/env jython

def perform(build, launcher, listener):
    if extension.getDescriptor().getUseFrench():
        listener.getLogger().println("Bonjour, " + extension.getName() + "!")
    else:
        listener.getLogger().println("Hello, " + extension.getName() + "!")
    return True
