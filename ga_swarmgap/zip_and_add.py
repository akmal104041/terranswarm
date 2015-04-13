import os
import paths
import sys
import shutil
import zipfile
import subprocess
import configparser

def zip_and_add(config_file, commit_mode, no_pull=False, no_add=False, no_commit=False):
    """
    Zips the files in output directory specified in config_file,
    copies it to our results/ directory and adds it to git and performs a commit.
    (git pull origin master is performed before add; git push must be manually performed)
    Parameters can be set to disable auto pull, add and commit
    :param config_file: path to the .xml config file
    :return:
    """

    config = configparser.ConfigParser(config_file)

    exp_out = paths.experiment_output_path(config)
    #print config.output_dir

    ### CODIGO PRA CRIAR O ARQUIVO .ZIP ###
    zip_path = '%s.zip' % exp_out
    #zip_file = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    #TODO: <<<adicionar os arquivos no zip_file
    ##zip_file.write(exp_out + "\\results.txt")

    shutil.make_archive(exp_out, "zip", exp_out)
    
   # zip_file.close()

   #copies zip_file to results/
    try:
        copied_zip_path = os.path.join('results', '%s.zip' % config.output_dir)
        shutil.copyfile(zip_path, copied_zip_path)
    except IOError as e:
        print 'An error has occurred. Could not copy %s \n' \
              'to %s' % (zip_path, copied_zip_path)
        raise e

    if (commit_mode == 'git'):
        #performs a git pull
        if not no_pull:
            subprocess.call(['git', 'pull', 'origin', 'master'])
            print 'pull attempted'

        #performs a git add
        if not no_add:
            subprocess.call(['git', 'add', copied_zip_path])
            print 'Attemped to add files to git'

            #performs a git commit
            if not no_commit:
                subprocess.call(['git', 'commit', '-m', 'Result file %s' % copied_zip_path])
                print 'git commit attempted, you must push manually'

    elif (commit_mode == 'svn'):
        #performs svn up
        if not no_pull:
            subprocess.call(['svn', 'up'])
            print 'up attempted'

        #performs a git add
        if not no_add:
            subprocess.call(['svn', 'add', copied_zip_path])
            print 'Attemped to add files to svn'

        #performs a git commit
        if not no_commit:
            subprocess.call(['svn', 'commit', '-m', 'Result file %s' % copied_zip_path])
            print 'svn commit attempted'

if __name__ == "__main__":
   
    num_configs = len(sys.argv)
    commit_mode = sys.argv[1]    

    for n in range(2,num_configs):
        zip_and_add(sys.argv[n], commit_mode, False, False, False)