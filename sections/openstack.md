# Openstack

Page's sections are ordered for my personal usages (not an alphabetical order)
and to get a quick access to things that I often need.

## Openstack reviews
- [Releases Reviews Inbox](https://review.opendev.org/#/dashboard/?title=Releases+Inbox&foreach=is%3Aopen&ussuri=project%3Aopenstack%2Freleases+file%3A%5Edeliverables%2Fussuri%2F.%2A+NOT+label%3AWorkflow%2D1&train=project%3Aopenstack%2Freleases+file%3A%5Edeliverables%2Ftrain%2F.%2A+NOT+label%3AWorkflow%2D1&stein=project%3Aopenstack%2Freleases+file%3A%5Edeliverables%2Fstein%2F.%2A+NOT+label%3AWorkflow%2D1&rocky=project%3Aopenstack%2Freleases+file%3A%5Edeliverables%2Frocky%2F.%2A+NOT+label%3AWorkflow%2D1&independent=project%3Aopenstack%2Freleases+file%3A%5Edeliverables%2F_independent%2F.%2A+NOT+label%3AWorkflow%2D1&Tools%2FJobs=%28%0A%28+project%3Aopenstack%2Dinfra%2Fproject%2Dconfig+file%3A%5Ezuul%2Fscripts%2Frelease%2Dtools%2F.%2A+%29%0AOR%0Aproject%3Aopenstack%2Dinfra%2Frelease%2Dtest%0AOR%0A%28+project%3Aopenstack%2Freleases+file%3A%5Eopenstack_releases%2F.%2A+%29%0AOR%0Aproject%3Aopenstack%2Freno%0A%29&All+Releases=is%3Aopen+project%3Aopenstack%2Freleases)
- [Requirements reviews](https://review.opendev.org/#/q/project:openstack/requirements)
- [RPM reviews](https://review.opendev.org/#/q/project:openstack/rpm-packaging)
- [Oslo Reviews Inbox](https://review.opendev.org/#/dashboard/?foreach=(project:%5Eopenstack/oslo.*+OR+project:openstack/debtcollector+OR%0Aproject:openstack/pylockfile+OR+project:openstack/castellan+OR%0Aproject:openstack/futurist+OR+project:openstack/automaton+OR%0Aproject:openstack/stevedore+OR+project:openstack/taskflow+OR%0Aproject:openstack/tooz+OR+project:openstack-dev/cookiecutter+OR%0Aproject:openstack-dev/pbr+OR+project:openstack/debtcollector+OR%0Aproject:openstack-dev/oslo-cookiecutter+OR+project:openstack/mox3)%0Astatus:open+NOT+owner:self+NOT+label:Workflow%3C=-1+label:Verified%3E=1%0ANOT+reviewedby:self&title=Oslo+Review+Inbox&Oslo+Specs=project:openstack/oslo-specs&Bug+Fixes=topic:%5Ebug/.*&Blueprints=message:%22Blueprint%22&Needs+Feedback+(Changes+older+than+5+days+that+have+not+been+reviewed+by+anyone)=NOT+label:Code-Review%3C=2+age:5d&You+are+a+reviewer,+but+haven't+voted+in+the+current+revision=reviewer:self&Needs+final+%2B2=label:Code-Review%3E=2+limit:50&New+Contributors=reviewer:10068&Passed+Jenkins,+No+Negative+Feedback=NOT+label:Code-Review%3E=2+NOT+label:Code-Review%3C=-1+limit:50&Wayward+Changes+(Changes+with+no+code+review+in+the+last+2days)=NOT+label:Code-Review%3C=2+age:2d)
- [Infra reviews](https://review.opendev.org/#/q/project:openstack/project-config)
- [Puppet-oslo](https://review.opendev.org/#/q/project:openstack/puppet-oslo)
- [Followed contributors](https://review.opendev.org/#/dashboard/?title=hberaud+Inbox&Sean=is:open+owner:%22Sean+McGinnis+%253Csean.mcginnis%2540gmail.com%253E%22+NOT+reviewedby:self+label:Verified%3E=1&Andreas=owner:%22Andreas+Jaeger+%253Cjaegerandi%2540gmail.com%253E%22+is:open+NOT+reviewedby:self+label:Verified%3E=1&Gmann=owner:%22Ghanshyam%20Mann%20%3Cgmann@ghanshyammann.com%3E%22+is:open+NOT+reviewedby:self+label:Verified%3E=1&Dmitriy=owner:%22Dmitriy+Rabotyagov+(noonedeadpunk)%22+status:open+is:open+NOT+reviewedby:self+label:Verified%3E=1)
- [Openstacksdk reviews](https://review.opendev.org/#/q/project:openstack/openstacksdk)
- [Openstackclient reviews](https://review.opendev.org/#/dashboard/?title=clients&Openstackclient=project:openstack/openstackclient+is:open&python-openstackclient=project:openstack/python-openstackclient+is:open)
- [experimental](https://review.opendev.org/#/dashboard/?title=Release/Requirements/Rpm-packaging%20Inbox&foreach=is:open+NOT+reviewedby:self&Releases=is:open%20project:openstack/releases&Requirements=is:open%20project:openstack/requirements&Rpm-packaging=is:open%20project:openstack/rpm-packaging)

## Release Management
- [core team members](https://review.opendev.org/#/admin/groups/11,members)
- [reno issues during sdist](https://storyboard.openstack.org/#!/story/2007274)
- [stable branches docs](https://docs.openstack.org/project-team-guide/stable-branches.html)
- [stable branches policy](https://governance.openstack.org/tc/reference/tags/stable_follows-policy.html)
- [Release processes - week per weeks steps](https://releases.openstack.org/reference/process.html)
- [Ussuri release management team's calendar](https://etherpad.openstack.org/p/ussuri-relmgt-tracking)
- [Example of cycle management that I've done on ussuri](https://etherpad.openstack.org/p/cycle-with-intermediary-deliverables)
- [Release canary test](https://review.opendev.org/#/c/721299/2/deliverables/ussuri/release-test.yaml)
- [QA releases](https://wiki.openstack.org/wiki/QA/releases)
- [openstack-announce - OpenStack Ussuri is officially released!](http://lists.openstack.org/pipermail/openstack-announce/2020-May/002035.html)
- [openstack-announce - OpenStack Victoria is officially released!](http://lists.openstack.org/pipermail/openstack-announce/2020-October/002041.html)
- [Project stopwatch](https://review.opendev.org/#/c/718929/)
- [Wallaby release management tracking - Draft](https://etherpad.opendev.org/p/wallaby-relmgt-tracking-draft)
- [release' zuul builds](https://zuul.opendev.org/t/openstack/builds?project=openstack%2Freleases)
- [zuul release-openstack-python](https://zuul.opendev.org/t/openstack/builds?job_name=release-openstack-python)
- [Release-job-failures ML](http://lists.openstack.org/cgi-bin/mailman/listinfo/release-job-failures)
- [Maintenance phases](https://docs.openstack.org/project-team-guide/stable-branches.html#maintenance-phases)
- [check-release-approval](https://zuul.openstack.org/builds?job_name=check-release-approval)
- [indicate relmgt style for each deliverable - abandon project](https://review.opendev.org/c/openstack/governance/+/613268)
- [Automatize branch deletion](http://lists.openstack.org/pipermail/openstack-discuss/2021-January/020034.html)
- [cycle-with-rc and major releases](https://docs.openstack.org/project-team-guide/release-management.html#services-horizon-plugins-and-other-deliverables)
- [OpenStack has a 6-month long release cadence](https://github.com/openstack/contributor-guide/blob/15f217ef3ebb0fb699a5b5fb0165de7abcbdc92d/doc/source/common/releases.rst)
- [Ironic release model](https://specs.openstack.org/openstack/ironic-specs/specs/15.1/new-release-model.html)

### Release meetings
- [wallaby meeting tracking](https://etherpad.opendev.org/p/wallaby-relmgt-tracking)
- [old victoria meeting example](http://eavesdrop.openstack.org/irclogs/%23openstack-release/%23openstack-release.2020-10-08.log.html#t2020-10-08T16:00:04)
- [wallaby schedule](https://releases.openstack.org/wallaby/schedule.html)
- [release meetings logs](http://eavesdrop.openstack.org/irclogs/%23openstack-release/)
- [Example of update irc-meeting](https://review.opendev.org/c/opendev/irc-meetings/+/766490)

### RDO
- [RDO victoria](https://github.com/redhat-openstack/rdoinfo/blob/master/tags/victoria.yml#L1142)

## Reviews on underlaying libraries (pull requests & issues)
- [cpython pull requests ](https://github.com/python/cpython/pulls)
- [cpython issues](https://bugs.python.org/)
- [eventlet pull requests](https://github.com/eventlet/eventlet/pulls)
- [eventlet issues](https://github.com/eventlet/eventlet/issues)
- [kombu pull requests](https://github.com/celery/kombu/pulls) 
- [kombu issues](https://github.com/celery/kombu/issues)
- [py-amqp pull requests](https://github.com/celery/py-amqp/pulls)
- [py-amqp issues](https://github.com/celery/py-amqp/issues)

## Requirements management

- [Updated from generate-constraints](https://review.opendev.org/#/c/748113/)

## RPM packaging

- [meeting pad](https://etherpad.opendev.org/p/openstack-rpm-packaging)
- [branching sample](https://review.opendev.org/#/c/645896/)

## Stats & status
- [RPM packaging status](https://toabctl.de/openstack/rpm-packaging-status-ussuri.html)
- [Ben Nemec's Oslo review stats](http://nemebean.com/reviewstats/oslo-open.html)

## General
- [Network management](https://www.weave.works/)
- [Openstack 1 server](http://docs.openstack.org/developer/devstack/guides/single-machine.html)
- [openstack command line cheat sheet](https://www.golinuxcloud.com/openstack-command-line-cheat-sheet/)
- [doc guideline](https://specs.openstack.org/openstack/docs-specs/specs/pike/os-manuals-migration.html)
- [zuul history](https://opensource.com/article/20/2/zuul)
- [TC - python version process update on openstack](https://governance.openstack.org/tc/resolutions/20181024-python-update-process.html)
- [The OpenStack Landscape](https://www.openstack.org/software/)

## Contribution guides
- [OpenStack Style Guidelines](https://docs.openstack.org/hacking/latest/user/hacking.html#styleguide)
- [Contributing Guide](https://docs.openstack.org/horizon/latest/contributor/contributing.html)
- [Code conventions](https://docs.openstack.org/doc-contrib-guide/writing-style/code-conventions.html)
- [Writing style](https://docs.openstack.org/doc-contrib-guide/writing-style.html)
- [Reviews guidelines](https://docs.openstack.org/doc-contrib-guide/docs-review-guidelines.html)
- [Four Opens Book](https://www.openstack.org/four-opens/)
- [Using temporary files securely](https://security.openstack.org/guidelines/dg_using-temporary-files-securely.html)

## Security
- [Security notes](https://github.com/openstack/security-doc/tree/master/security-notes)

## Status
- [openstack status](http://status.openstack.org/)
- [openstack health check](http://status.openstack.org/openstack-health/#/)
- [reviews status](http://status.openstack.org/reviews/)
- [zuul status](https://zuul.openstack.org/projects)

## Oslo
- [openstack review guide/tips](https://docs.openstack.org/project-team-guide/review-the-openstack-way.html)
- [oslo guide](https://docs.openstack.org/project-team-guide/oslo.html)
- [openstack-discuss ML official topics](https://etherpad.openstack.org/p/common-openstack-ml-topics)
- [openstack wide goal](https://governance.openstack.org/tc/goals/index.html)
- [oslo specs](https://specs.openstack.org/openstack/oslo-specs/)
- [stable branches reviews guidelines](https://docs.openstack.org/project-team-guide/stable-branches.html#review-guidelines)
- [Libraries & focus](https://etherpad.openstack.org/p/oslo-pike-tracking)
- [meeting](https://wiki.openstack.org/wiki/Meetings/Oslo)
- [Liaisons](https://specs.openstack.org/openstack/oslo-specs/specs/policy/liaisons.html)
- [meetings logs](http://eavesdrop.openstack.org/meetings/oslo/2018/)
- [feature freeze specifications](https://specs.openstack.org/openstack/oslo-specs/specs/policy/feature-freeze.html)
- [python 3 status](https://wiki.openstack.org/wiki/Python3#Python_3_Status_of_OpenStack_projects)
- [release reviews](https://review.openstack.org/#/q/project:openstack/releases+status:open)
- [stackalytic - reviews average](http://stackalytics.com/)
- [Oslo wiki](https://wiki.openstack.org/wiki/Oslo)
- [Oslo core members](https://review.opendev.org/#/admin/groups/106,members)
- [Moises's oslo.config speak at fosdem](https://fosdem.org/2020/schedule/event/security_protecting_plaintext_secrets_in_configuration_files/)
- [Oslo/blueprints/asyncio](https://wiki.openstack.org/wiki/Oslo/blueprints/asyncio)
- [asyncio-executor](https://blueprints.launchpad.net/oslo.messaging/+spec/asyncio-executor)

## Testing
- [understand the openstack CI system](http://www.joinfu.com/2014/01/understanding-the-openstack-ci-system/)
- [bindep](https://docs.openstack.org/infra/bindep/readme.html)
- [Zuul setup perdiodical job example 1](https://code.engineering.redhat.com/gerrit/#/c/168584/)
- [Zuul setup perdiodical job example 2](https://code.engineering.redhat.com/gerrit/169014)
- [Zuul setup perdiodical job example 3](https://code.engineering.redhat.com/gerrit/169766)
- [https://wiki.openstack.org/wiki/Testr#Debugging_.28pdb.29_Tests](https://wiki.openstack.org/wiki/Testr)
- [pdb/tox/stestr - no way to drop into a debugger safely](https://bugs.launchpad.net/testrepository/+bug/902881)

## Tooling
- [isort autopep on tempest](https://opendev.org/openstack/tempest/src/branch/master/tools/format.sh)
- [Codesearch - Hound](http://codesearch.openstack.org/?q=&i=nope&files=&repos=)

## Infra
- [OpenStack Infra Config Files](https://github.com/4383/project-config)
- [Openstack Grafana](http://grafana.openstack.org/)
- [Openstack IRC bot (Gerritbot)](https://docs.openstack.org/infra/system-config/irc.html)
- [Tested runtimes - Victoria](https://governance.openstack.org/tc/reference/runtimes/victoria.html)
- [SUSE Cloud CI](https://wiki.openstack.org/wiki/ThirdPartySystems/SUSE_Cloud_CI)
- [Infra logstation filters](https://opendev.org/openstack/logstash-filters/src/branch/master/filters/openstack-filters.conf)

## Governance
- [OpenStack Election](https://governance.openstack.org/election/)
- [Openstack SIG](https://governance.openstack.org/sigs/)
- [Distributed Project Lead (DPL)](https://governance.openstack.org/tc/resolutions/20200803-distributed-project-leadership.html)
- [Deprecating a repository](https://docs.openstack.org/project-team-guide/repository.html#deprecating-a-repository)

## /tmp
- [[oslo.messaging][RDO] Add pyngus to rhel > 7](https://review.rdoproject.org/r/#/c/22745/)

## Devstack
- [Ben Nemec's multi devstack host blog post](http://blog.nemebean.com/content/multi-host-devstack)
- [Ben Nemec's Devstack VMs setup scripts](https://fedorapeople.org/~bnemec/devstack-base/)

## red Hat
- [OSP13 - High Availability Deployment and Usage](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/13/html-single/high_availability_deployment_and_usage/index)
- [OSP15 - High Availability Deployment and Usage](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/15/html-single/high_availability_deployment_and_usage/index)
- [OSP16 - High Availability Deployment and Usage](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.0/html-single/high_availability_deployment_and_usage/index)
- [OSP16.1 - Doc](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/director_installation_and_usage/chap-introduction#sect-Overcloud)

## Finances
- [OpenStack Market Size & Share Analysis & Gross Revenues Development Forecast, 2020 to 2026](https://rejerusalem.com/73943/openstack-market-size-share-analysis-gross-revenues-development-forecast-2020-to-2026/)

## Bugs

- [OpenStack Nova deadlock in powervc_oslo when enabling OpenStack debug mode (threading.enumerate() deadlock)](https://bugzilla.redhat.com/show_bug.cgi?id=1959459)
