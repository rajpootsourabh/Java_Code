package com.programs;

// Create class-01
class Employee{
    int salary;
    String name;
    // Method
    public int getSalary(){
        return salary;
    }
    // Method
    public String getName() {
        return name;
    }
    // Method
    public void setName(String n){
        name = n;
    }
}

// Create class-02
class cellphone {
    // Method
    public void ringing() {
        System.out.println("Ringing");
    }
    // Method
    public void calling() {
        System.out.println("Calling......+91 -8726454894");
    }
}

// Create Class Square
class square{
    int side;
    // Method
    public int getArea(){
        return side*side;
}
    public int perimeter(){
        return 4*side;
    }
}

public class Practice_Set {
    public static void main(String[] args) { // Built-in main method
        // Create Object for Class Employee
        Employee Sourabh = new Employee();
        Sourabh.setName("Sourabh Singh"); // Call method and print
        System.out.println("Name: "+Sourabh.getName()); // Call method and print
        Sourabh.salary = 900000;
        System.out.println("Salary: "+Sourabh.getSalary()+" LPA"); // Call method and print

        // Create Object for Class Cellphone
        cellphone Vivo = new cellphone();
        Vivo.ringing(); // Call method
        Vivo.calling(); // Call method

        // Create Object for Class Square
        square S = new square();
        S.side = 8;
        System.out.println("Area: "+S.getArea()); // Call method and print
        System.out.println("Perimeter: "+S.perimeter()); // Call method and

    }
}
