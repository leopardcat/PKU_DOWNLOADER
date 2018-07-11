说明
1.Indexbasement_Maintenance.jar 建库工具
    生产力更高。
2.is_cve_contains_android.py 检测 start ~ end 的 cve条目是否为andriod.
    1)输入 开始条目 （较大的） 如 cve-2014-5600 输入 5600
    2)输入 结束条目 （较小的） 如 cve-2014-5500 输入 5500
    会显示出 从cve-2014-5600 到 cve-2014-5500 描述中有andriod的条目
3.基本同 2 只是显示的为不含andriod的条目
注:python脚本不适用时自己可简单修改。



//可忽视以下
//测试里的
 public String sub_string(String string, String newversion)
    {
        



        String pattern = "\\d+\\.([a-z])\\-";
        string = string.replaceAll(pattern,"");
        System.out.println(string);
        String pattern1 = "(v)?\\d+(\\-)(\\d+)(\\-([a-z]|\\d+))?(\\-([a-z]|\\d+))?";
        String pattern2 = "(v)?\\d+(\\_)(\\d+)(\\_([a-z]|\\d+))?(\\_([a-z]|\\d+))?";
        String pattern3 = "(v)?[1-9]?(\\.)([1-9]+)(\\.([a-s,u-x]|\\d+))?([a-z]\\d+)?";
        //String pattern3 = "(v)?\\d+(\\.)(\\d+)(\\.(\\d+)(\\.\\d+))";

        String newversion1 = newversion.replace('.','-');
        String newversion2 = newversion.replace('.','_');
        string = string.replaceAll(pattern1,newversion1).replaceAll(pattern2,newversion2).replaceAll(pattern3,newversion);

        return string;
    }

// 项目里的
public static String sub_string(String string,String newversion)
    {
        String pattern = "\\d+\\.([a-z])\\-";
        string = string.replaceAll(pattern,"");

        String pattern1 = "(v)?\\d+(\\-)(\\d+)(\\-([a-z]|\\d+))?";
        String pattern2 = "(v)?\\d+(\\_)(\\d+)(\\_([a-z]|\\d+))?";
        //String pattern3 = "(v)?[1-9]?(\\.)([1-9]+)(\\.([a-s,u-x]|\\d+))?([a-z]\\d+)?";
        String pattern3 = "(v)?\\d+(\\.)(\\d+)(\\.([a-s,u-x]|\\d+))?([a-z]\\d+)?";

        //String pattern3 = "(v)?\\d+(\\.)(\\d+)(\\.([a-s,u-x]|\\d+))?([a-z]\\d+)?";
        //String pattern3 = "(v)?\\d+(\\.)(\\d+)(\\.(\\d+)(\\.\\d+))";

        String newversion1 = newversion.replace('.','-');
        String newversion2 = newversion.replace('.','_');
        string = string.replaceAll(pattern1,newversion1).replaceAll(pattern2,newversion2).replaceAll(pattern3,newversion);

        return string;
    }
//
7.11
//
String pattern = "\\d+\\.([a-z])\\-";
        string = string.replaceAll(pattern,"");

        String pattern1 = "(v)?\\d+(\\-)(\\d+)(\\-([a-z]|\\d+))?(\\-([a-z]|\\d+))?";
        String pattern2 = "(v)?\\d+(\\_)(\\d+)(\\_([a-z]|\\d+))?(\\_([a-z]|\\d+))?";
        //String pattern3 = "(v)?[1-9]?(\\.)([1-9]+)(\\.([a-s,u-x]|\\d+))?([a-z]\\d+)?";
        String pattern3 = "(v)?\\d+(\\.)(\\d+)(\\.([a-s,u-x]|\\d+))?([a-z]\\d+)?";
        String pattern41 = "(v)\\d+^\\/|(\\.)(\\d+)^\\/|(\\.([a-s,u-x]|\\d+))?([a-z]\\d+)?";
        String pattern42 = "(V)\\d+^\\/|(\\.)(\\d+)^\\/|(\\.([a-s,u-x]|\\d+))?([a-z]\\d+)?";
        boolean isMatch1 = Pattern.compile(pattern41).matcher(string).lookingAt();
        boolean isMatch2 = Pattern.compile(pattern42).matcher(string).lookingAt();

        if(isMatch1)
        {
            if (!(newversion.substring(0, 1).equals("v")) && !newversion.substring(0, 1).equals("V"))
            {
                newversion = 'v' + newversion;
            }
        }
        if(isMatch2)
        {
            if (!(newversion.substring(0, 1).equals("v")) && !newversion.substring(0, 1).equals("V"))
            {
                newversion = 'V' + newversion;
            }
        }

        String newversion1 = newversion.replace('.','-');
        String newversion2 = newversion.replace('.','_');
        string = string.replaceAll(pattern1,newversion1).replaceAll(pattern2,newversion2).replaceAll(pattern3,newversion);

        return string;
    }