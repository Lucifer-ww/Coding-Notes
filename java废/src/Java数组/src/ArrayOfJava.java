public class ArrayOfJava<myList> {
    public static void main(String []args) {
        System.out.println("Hello world");
    }//框架-一定要记住
    //dataType[]arrayRefVar 首选方法
    int size = 10;
    double[]myList = new double[size];
    //arrayRefVar = new dataType[arraySize];
    myList[0] = 5.6;
    myList[1] = 4.5;
    myList[2] = 3.3;
    myList[3] = 13.2;
    myList[4] = 4.0;
    myList[5] = 34.33;
    myList[6] = 34.0;
    myList[7] = 45.45;
    myList[8] = 99.993;
    myList[9] = 11123.0;
    // 计算所有元素的总和
    double total = 0.0;
      for (int i = 0; i < size; i++) {
        total += myList[i];
    }
      System.out.println("总和为： " + total);
}