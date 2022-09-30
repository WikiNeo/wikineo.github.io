import os
import glob


class TagFileGenerator:
    """Acknowledgement

    tag_generator.py
    Copyright 2017 Long Qian
    Contact: lqian8@jhu.edu
    This script creates tags for your Jekyll blog hosted by GitHub page.
    No plugins required.
    """
    def __init__(self, tag_dir: str):
        self.tag_dir = tag_dir
        self.filenames = []

        self.__create_tag_dir_if_not_exist()
        self.__remove_old_tags()
        self.__add_new_tags()

        self.__log()

    def __log(self):
        print("Tags generated, count", self.all_tags.__len__())

    def __add_new_tags(self):
        """generate new tag files

        :return:
        """
        self.__set_filenames()
        self.all_tags = self.__get_all_tags()

        # generate tag files with content
        for tag in self.all_tags:
            tag_filename = self.tag_dir + tag + '.md'

            with open(tag_filename, 'a', encoding='utf-8') as f:
                write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + \
                            '\nrobots: noindex\n---\n'
                f.write(write_str)

    def __remove_old_tags(self):
        """remove old tag files in tag_dir
        """
        old_tags = glob.glob(self.tag_dir + '*.md')
        for old_tag in old_tags:
            os.remove(old_tag)

    def __create_tag_dir_if_not_exist(self):
        """create tag_dir if not exist
        """
        if not os.path.exists(self.tag_dir):
            os.makedirs(self.tag_dir)

    def __set_filenames(self):
        """save all files ending with .md and .html to filenames list
        """
        post_dir = '_posts/*/*'
        file_types = ['.md', '.html']
        for file_type in file_types:
            self.filenames.extend(glob.glob(post_dir + file_type))

    def __get_all_tags(self) -> set:
        """Store values in between --- & --- starting with tags: to total_tags
        """
        total_tags = []
        for filename in self.filenames:
            with open(filename, 'r', encoding='utf8') as f:
                crawl = False
                for line in f:
                    if crawl:
                        current_tags = line.strip().split()
                        if current_tags[0] == 'tags:':
                            total_tags.extend(current_tags[1:])
                            crawl = False
                            break
                    if line.strip() == '---':
                        if not crawl:
                            crawl = True
                        else:
                            crawl = False
                            break
        self.a = []
        return set(total_tags)


TagFileGenerator('tag/')
