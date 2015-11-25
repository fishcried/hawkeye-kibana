# What's hawk-kibana

# 可视化定义规则

**<preffix>-[scope]-<desc>**

- preffix
    - sch search
    - vsz visualizaton
    - dbd dashboard
- scope
    - all
    - service
- desc

# 已定义的search,visualization,dashboard

**searches**

- sch-all-entry 
   所有日志,fields: time, message, loglevel, path, host
- sch-ops-entry
   openstack日志,fields: time, message, loglevel, path, host
- sch-ops-bomb

**visualization**

- vsz-all-navigation
   导航
- vsz-ops-magic-cycle
   内到外: level -> type -> path -> host

- vsz-all-by-hosts
- vsz-ops-by-hosts
- vsz-ops-by-types
- vsz-ops-by-paths
- vsz-ops-by-reqids

- vsz-ops-by-http-codes
- vsz-ops-by-http-methods
- vsz-ops-by-http-reponses
- vsz-ops-by-http-bytes
- vsz-ops-api-top10

- vsz-ops-bomb-by-paths
- vsz-ops-bomb-by-hosts
- vsz-ops-bomb-by-types
- vsz-ops-bomb-by-api-top10

- vsz-horizon-action-by-users
- vsz-rabbitmq-action-by-sip


**dashboard**

- dbd-ops-ovewview
- dbd-ops-debug
- dbd-nova
- dbd-neutron
- dbd-glance
- dbd-cinder
- dbd-ceilometer
- dbd-keystone
- dbd-horizon
- dbd-rabbitmq
- dbd-auth

# 如何便捷导入

当前预定义的内容都分别存放在json目录中，当进行kibana导入的时候如何一个一个的导入很麻烦。可以通过`tools/convert.py`将这么json文件合并成一个文件，然后进行导入即可。

合并操作

    cd tools
    python convert.py --func join -d ../json -f all.py

同时convert.py也可以进行split操作 

    cd tools
    python convert.py --func split -d tmp -f all.py
