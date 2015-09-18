# rpm_device is the name of the ported device
%define rpm_device moto_msm8960_jbbl

# rpm_vendor is used in the rpm space
%define rpm_vendor motorola

# Manufacturer and device name to be shown in UI
%define vendor_pretty Motorola
%define device_pretty Photon Q

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 1
%define have_led 1

%define android_config \
#define QCOM_BSP 1\
%{nil}

%include droid-hal-version/droid-hal-version.inc
