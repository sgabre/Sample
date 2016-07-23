import os
import subprocess
import ConfigParser

def get_git_revision_hash():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD'])

def get_git_revision_short_hash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])



if __name__ == '__main__':
    ExecutionDirectory=os.getcwd()
    print "Execution Directory: " + ExecutionDirectory 
    SourcePath="../src/Configuration/"  
    print "Generate Build Version.h"
    # Open a file
    BuildVersionHeaderFile = open(SourcePath+"BuildVersion.h", "wb")
    BuildVersionHeaderFile.write( "#ifndef BUILDVERSION_H_\n");
    BuildVersionHeaderFile.write( "#define BUILDVERSION_H_\n");
    BuildVersionHeaderFile.write( "extern const char * BuildDate;\n");
    BuildVersionHeaderFile.write( "extern const char * BuildLongVersion;\n");
    BuildVersionHeaderFile.write( "extern const char * BuildShortVersion;\n");
    BuildVersionHeaderFile.write( "#endif /* BUILDVERSION_H_ */\n");
        # Close opend file
    BuildVersionHeaderFile.close()
    
    print "Generate Build Version.c"
    BuildVersionSourceFile = open(SourcePath+"BuildVersion.c", "wb")
    BuildVersionSourceFile.write( "#include \"./Configuration/BuildVersion.h\"\n");
    BuildVersionSourceFile.write( "const char * BuildDate = \"2009-11-10 11:09\";\n");
    BuildLongVersion = get_git_revision_hash()
    BuildShortVersion = get_git_revision_short_hash()
    
    BuildLongVersion = BuildLongVersion[:-1]
    BuildLongVersionString = "const char * BuildLongVersion = \"%s\";\n" % (BuildLongVersion)
    BuildVersionSourceFile.write(BuildLongVersionString);
    
    BuildShortVersion = BuildShortVersion[:-1]
    BuildShortVersionString = "const char * BuildShortVersion = \"%s\";\n" % (BuildShortVersion)
    BuildVersionSourceFile.write(BuildShortVersionString);
    
    
    # Close opend file
    BuildVersionSourceFile.close()
    pass