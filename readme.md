 public String sub_string(String string, String newversion)
    {
        


        String pattern = "\\^.\\d+\\.([a-z]|\\d+)\\-";
        string = string.replaceAll(pattern,"");
        String pattern1 = "(v)?\\d+(\\-)(\\d+)(\\-([a-z]|\\d+))?";
        String pattern2 = "(v)?\\d+(\\_)(\\d+)(\\_([a-z]|\\d+))?";
        String pattern3 = "(v)?\\d+(\\.)(\\d+)(\\.([a-s,u-x]|\\d+))?";

        String newversion1 = newversion.replace('.','-');
        String newversion2 = newversion.replace('.','_');
        string = string.replaceAll(pattern1,newversion1).replaceAll(pattern2,newversion2).replaceAll(pattern3,newversion);

        return string;
    }