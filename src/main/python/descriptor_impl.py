#!/usr/bin/env jython

import hudson.util.FormValidation as FormValidation

def descriptor_impl():
    extension.load();

def configure(request, formData):
    extension.setUseFrench(formData.getBoolean("useFrench"))
    extension.save();
    return extension.superConfigure(request, formData)

def is_applicable(_class):
    return True
    
def get_display_name():
    return "Execute InstallShield builder"

def do_check_name(value):
    if len(value) == 0:
        return FormValidation.error("Please set a name")
    if len(value) < 4:
        return FormValidation.warning("Isn't the name too short?")
    return FormValidation.ok()
