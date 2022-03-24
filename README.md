## SensUs competition 2020 code

### Objectives
- the main code is modified from SensUs 2019 and adds real time image acquisition feature
- live stream mode for focus tuning
- capture mode and image processing for concentration computing
### How to use
- install required spinnaker SDK and corresponding python package
- check usbfs memory with "/sys/module/usbcore/parameters/usbfs_memory_mb" if not enough change it according to "https://www.flir.com/support-center/iis/machine-vision/application-note/understanding-usbfs-on-linux/"
- increase socket send buffer size if not enough with "sysctl -w net.core.rmem_default=26214400"
### Dependencies
- python3
- pygame
- scikit-image
- matplotlib

