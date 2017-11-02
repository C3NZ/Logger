'''
Module - logger.py

Description - Module for logging information to the console or txt file

Items -

    Class Logger:
        -Logger Description-
            This class is used for writing text to either the console or txt file.
            You do not instantiate any Logger objects for use but rather call each function
            statically.

        -Logger  static variables-
            TYPE : NAME - DESC
            string : directory - directory the log files will be written to
            string : fileName - The name of the log file
            file object : f - File object for the logger to write to
            boolean : forceConsole - Forces log_* functions to print to the console
                                     as well as write to a txt file.


        -Logger functions-
            RETURNTYPE : NAME - DESC
            void : console_i - prints information to the console
            void : console_e - prints error information to the console
            void : console_d - prints debug information to the console
            void : log_info - writes information to a txt file
            void : log_error - writes error information to a txt file
            void : log_debug - writes debug information to a txt file
            void : close_log - Closes the file object

'''

from inspect import getframeinfo, stack
from time import strftime
from os.path import abspath, join

#Class to log information to both a text file and the users console
class Logger(object):
    '''
       If the console is only being called explicitly, the only
       argument that needs to be passed is a string containing the
       information you're trying to print out

       arg[0] = message - output to the console
       arg[1] = file name - what file the logger instance was called from
       arg[2] = line number - what linea logger instance was called from

    '''
    DEBUGMODE = True
    directory = "logs/"
    file_name = "{}.txt".format(strftime("%m-%d-%Y"))
    file_object = open(join(directory, file_name), "a+")
    forceConsole = True

    @staticmethod
    def reload_file_object(directory=None, file_name=None):
        """
        Reload the file object used for appending data to

        Params:
            directory = directory path as a string
            file_name = file_name as a string
        """
        if directory is None and file_name is None:
            Logger.file_object = open(join(Logger.directory, Logger.file_name), 'a+')
        elif directory is not None and file_name is None:
            Logger.file_object = open(join(directory, Logger.file_name), 'a+')
        elif directory is None and file_name is not None:
            Logger.file_object = open(join(Logger.directory, file_name), 'a+')
        else:
            Logger.file_object = open(join(directory, file_name), 'a+')

    #Write info to the console
    @staticmethod
    def console_i(*args):
        if len(args) == 1:
            caller = getframeinfo(stack()[1][0])
            print("[INFO][{}][{}]:{}".format(caller.filename, caller.lineno, args[0]))
        else:
            print("[INFO][{}][{}]:{}".format(args[2], args[1], args[0]))

    #Write an error to the console
    @staticmethod
    def console_e(*args):
        if len(args) == 1:
            caller = getframeinfo(stack()[1][0])
            print("[ERROR][{}][{}]:{}".format(caller.filename, caller.lineno, args[0]))
        else:
            print("[ERROR][{}][{}]:{}".format(args[2], args[1], args[0]))

    #Write debug info to the console
    @staticmethod
    def console_d(*args):
        if Logger.DEBUGMODE:
            if len(args) == 1:
                caller = getframeinfo(stack()[1][0])
                print("[DEBUG][{}][{}]:{}".format(caller.filename, caller.lineno, args[0]))
            else:
                print("[DEBUG][{}][{}]:{}".format(args[2], args[1], args[0]))

    #append information to a log file
    @staticmethod
    def log_info(message):
        caller = getframeinfo(stack()[1][0])
        if Logger.forceConsole:
            Logger.console_i(message, caller.filename, caller.lineno)
        Logger.f.write("[INFO][{}][{}][{}][{}]:{}\n".format(strftime("%m-%d-%Y"),
                        strftime("%H:%M:%S"), caller.filename, caller.lineno, message))

    #append error information to a log file
    @staticmethod
    def log_error(message):
        caller = getframeinfo(stack()[1][0])
        if Logger.forceConsole:
            Logger.console_e(message, caller.filename, caller.lineno)
        Logger.f.write("[ERROR][{}][{}][{}][{}]:{}\n".format(strftime("%m-%d-%Y"),
                        strftime("%H:%M:%S"), caller.filename, caller.lineno, message))

    #append debugging information to a log file
    @staticmethod
    def log_debug(message):
        caller = getframeinfo(stack()[1][0])
        if Logger.DEBUGMODE:
            if Logger.forceConsole:
                Logger.console_d(message, caller.filename, caller.lineno)
            Logger.f.write("[DEBUG][{}][{}][{}][{}]:{}\n".format(strftime("%m-%d-%Y"),
                            strftime("%H:%M:%S"), caller.filename, caller.lineno, message))

    #Close the logging file when it no longer needs to be accessed
    @staticmethod
    def close_log():
        Logger.f.close()