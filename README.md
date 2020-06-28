# EC2 metadata mock service
[![Build Status](https://travis-ci.org/pygillier/ec2-metamock.svg?branch=master)](https://travis-ci.org/pygillier/ec2-metamock)

This app aims to offer a mock service for EC2 metadata service directly on your computer.

For details on what is available in official service, see [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)

## Usage

Run:
```bash
$ ec2_metamock [--host=localhost] [--port=8080]
```


## Mocked keys

Reserved or deprecated keys aren't mocked.

|                         Key name                        | Mocked ? |                               Returned value                              | Comment |
|---------------------------------------------------------|----------|---------------------------------------------------------------------------|---------|
| ami-id                                                  | Yes      | `ami-0abcdef1234567890`                                                   |         |
| ami-launch-index                                        | Yes      | `0`                                                                       |         |
| ami-manifest-path                                       | Yes      | `(unknown)`                                                               |         |
| ancestor-ami-ids                                        |          |                                                                           |         |
| block-device-mapping/ami                                |          |                                                                           |         |
| block-device-mapping/ebsN                               |          |                                                                           |         |
| block-device-mapping/ephemeralN                         |          |                                                                           |         |
| block-device-mapping/root                               |          |                                                                           |         |
| block-device-mapping/swap                               |          |                                                                           |         |
| elastic-gpus/associations/elastic-gpu-id                |          |                                                                           |         |
| elastic-inference/associations/eia-id                   |          |                                                                           |         |
| events/maintenance/history                              |          |                                                                           |         |
| events/maintenance/scheduled                            |          |                                                                           |         |
| hostname                                                | Yes      | `ip-10.11.12.13.us-east-1.compute.internal`                               |         |
| iam/info                                                |          |                                                                           |         |
| iam/security-credentials/role-name                      |          |                                                                           |         |
| instance-action                                         | Yes      | `none`                                                                    |         |
| instance-id                                             | Yes      | `i-0235ba33af8e86af4`                                                     |         |
| instance-type                                           | Yes      | `t3.small`                                                                |         |
| kernel-id                                               |          |                                                                           |         |
| local-hostname                                          | Yes      | `ip-10.11.12.13.us-east-1.compute.internal`                               |         |
| local-ipv4                                              | Yes      | `10.11.12.13`                                                             |         |
| mac                                                     | Yes      | `e9:8b:53:68:9a:20`                                                       |         |
| network/interfaces/macs/mac/device-number               |          |                                                                           |         |
| network/interfaces/macs/mac/interface-id                |          |                                                                           |         |
| network/interfaces/macs/mac/ipv4-associations/public-ip |          |                                                                           |         |
| network/interfaces/macs/mac/ipv6s                       |          |                                                                           |         |
| network/interfaces/macs/mac/local-hostname              |          |                                                                           |         |
| network/interfaces/macs/mac/local-ipv4s                 |          |                                                                           |         |
| network/interfaces/macs/mac/mac                         |          |                                                                           |         |
| network/interfaces/macs/mac/owner-id                    |          |                                                                           |         |
| network/interfaces/macs/mac/public-hostname             |          |                                                                           |         |
| network/interfaces/macs/mac/public-ipv4s                |          |                                                                           |         |
| network/interfaces/macs/mac/security-groups             |          |                                                                           |         |
| network/interfaces/macs/mac/security-group-ids          |          |                                                                           |         |
| network/interfaces/macs/mac/subnet-id                   |          |                                                                           |         |
| network/interfaces/macs/mac/subnet-ipv4-cidr-block      |          |                                                                           |         |
| network/interfaces/macs/mac/subnet-ipv6-cidr-blocks     |          |                                                                           |         |
| network/interfaces/macs/mac/vpc-id                      |          |                                                                           |         |
| network/interfaces/macs/mac/vpc-ipv4-cidr-block         |          |                                                                           |         |
| network/interfaces/macs/mac/vpc-ipv4-cidr-blocks        |          |                                                                           |         |
| network/interfaces/macs/mac/vpc-ipv6-cidr-blocks        |          |                                                                           |         |
| placement/availability-zone                             | Yes      | `us-east-1`                                                               |         |
| product-codes                                           |          |                                                                           |         |
| public-hostname                                         |          |                                                                           |         |
| public-ipv4                                             | Yes      |                                                                           |         |
| public-keys/0/openssh-key                               |          |                                                                           |         |
| ramdisk-id                                              |          |                                                                           |         |
| reservation-id                                          | Yes      | `r-01c15d13beef4376d`                                                     |         |
| security-groups                                         | Yes      | `security-group-one,            'security-group-two,security-group-three` |         |
| services/domain                                         | Yes      |                                                                           |         |
| services/partition                                      | Yes      |                                                                           |         |
| spot/instance-action                                    |          |                                                                           |         |
| spot/termination-time                                   |          |                                                                           |         |

## Contributing

See [CONTRIBUTING.md](/CONTRIBUTING.md).
