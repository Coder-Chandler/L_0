import os
import os.path
import ConfigParser
'''
1:dump ini
2:del section
3:del item
4:modify item
5:add section
6:save modify
'''


class StudentInfo(object):

    def __init__(self, recordfile):
        self.logfile = recordfile
        self.cfg = ConfigParser.ConfigParser()

    def cfg_load(self):
        self.cfg.read(self.logfile)

    def cfg_dump(self):
        se_list = self.cfg.sections()
        print '====================>'
        for se in se_list:
            print se
            print self.cfg.items(se)
        print '<===================='

    def delete_item(self, section, key):
        self.cfg.remove_option(section, key)

    def delete_section(self, section):
        self.cfg.remove_section(section)

    def add_section(self, section):
        self.cfg.add_section(section)

    def set_item(self, section, key, value):
        self.cfg.set(section, key, value)

    def save(self):
        fp = open('self.logfile', 'w')
        self.cfg.write(fp)
        fp.close()
if __name__ == '__main__':
    info = StudentInfo('immoc.txt')
    info.cfg_load()
    info.cfg_dump()
    info.set_item('userinfo', 'pwd', '910929xiao!@')
    info.cfg_dump()
    info.add_section('login')
    info.set_item('login', '2017-0603', '200')
    info.cfg_dump()
    info.save()
