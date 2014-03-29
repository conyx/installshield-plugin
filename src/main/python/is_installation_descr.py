#!/usr/bin/env jython

def is_installation_descr():
    extension.load()

def get_display_name():
    return "InstallShield"

def set_installations(*installations):
    extension.superSetInstallations(installations)
    extension.save();
