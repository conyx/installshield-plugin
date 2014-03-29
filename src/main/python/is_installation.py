#!/usr/bin/env jython

def init_plugin():
    global ISInstallation
    ISInstallation = type(extension)

def for_node(node, log):
    return ISInstallation(extension.getName(), extension.translateFor(node, log))

def for_environment(environment):
    return ISInstallation(extension.getName(), environment.expand(extension.getHome()))
