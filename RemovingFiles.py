import os
import shutil 
import time

def main():

    deleted_folders_count = 0
    deleted_files_count = 0


    path = "/PATH_TO_DELETE"

    # specify the day
    days = 30

    # time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)


    # checking the existence of a path
    if os.path.exists(path):



        for root_folder, files , folders in os.walk(path):
            
            
            #comparison of days
            if seconds>= get_file_or_folder_age(root_folder):

                # remove the folder
                remove_folder(root_folder)

                # incrementing count
                deleted_folders_count += 1

                break

            else :

                for folder in folders :
                    folder_path = os.path.join(root_folder , folder)


                    if seconds >= get_file_or_folder_age(folder_path):

                        remove folder(folder_path)
                        deleted_folders_count += 1
                        
                        print(f"Unable to delete the"+path)


def remove_file(path):

     if not os.remove(path):

         print(f"{path} is removed successfully")

    else:

        print(f"Unable to delete the"+ path)


def get_file_or_folder_age(path):

    ctime = os.stat(path).st_ctime

    return ctime


if __name__ == '__main__':
    main()
