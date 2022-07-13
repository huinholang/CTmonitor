import certstream
import re
import sys
import argparse
import subprocess
from subprocess import Popen, PIPE

print("""\

 ╲┏━━┳━━━━━━━━━━┓╲╲     (  _`\(_   _)                        _ ( )_
 ╲┃◯ ┃ ╭┻┻╮╭┻┻╮ ┃╲╲     | ( (_) | |  ___ ___     _     ___  (_)| ,_)   _    _ __
 ╲┃╮ ┃ ┃╭╮┃┃╭╮┃ ┃╲╲     | |  _  | |/' _ ` _ `\ /'_`\ /' _ `\| || |   /'_`\ ( '__)
 ╲┃╯ ┃ ┗┻┻┛┗┻┻┻ ┻╮╲     | (_( ) | || ( ) ( ) |( (_) )| ( ) || || |_ ( (_) )| |
 ╲┃◯ ┃◯     ┏━━━┳╯╲     (____/' (_)(_) (_) (_)`\___/'(_) (_)(_)`\__)`\___/'(_)
 ╲┃╭ ┃  ┏┳┳┳┳┓◯┃╲╲      CTmonitor can help you to detect some typosquatting domain. You can use regular or irregular expressions.
 ╲┃╰ ┃◯╰┗┛┗┛╯╭ ┃╲╲      Huinholag 2022(C)

""")

def regex(regex):
        rex = re.compile(regex, re.IGNORECASE)
        orgin_stdout = sys.stdout
        file = open('CTmonitor-results.txt', 'a+')
        sys.stdout = file

        process = subprocess.Popen(['certstream'], stdout=subprocess.PIPE, universal_newlines=True)
        for website in process.stdout:
                if re.search(rex, website):
                        print (website)
                else:
                        pass

        sys.stdout = origin_stdout
        file.close()

def irregular(irregular):
        orgin_stdout = sys.stdout
        file = open('CTmonitor-results.txt', 'a+')
        sys.stdout = file

        process = subprocess.Popen(['certstream'], stdout=subprocess.PIPE, universal_newlines=True)
        for website in process.stdout:
                if website.strip() == irregular:
                        print(website)
                else:
                        pass

        sys.stdout = origin_stdout
        file.close()

def main():
        parser = argparse.ArgumentParser(prog='CTmonitor', description='CTmonitor can help you to detect some typosquatting domain. You can use regular or irregular expressions.')
        parser.add_argument('--regex','-r', type=regex, help='Add regular expression to search website.')
        parser.add_argument('--irregular', '-i', type=irregular, help='Add irregular expression to search website.')
        args = parser.parse_args()
        parser.print_help()

        if args.regex == True:
                regex()

        elif args.irregular == True:
                irregular()

if __name__ == '__main__':
    main()
