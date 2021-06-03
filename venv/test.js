var dayOfWeek = new Date();
dayOfWeek = dayOfWeek.getDay();
document.write(dayOfWeek);
switch(dayOfWeek){
    case 0:
        document.write("Sunday");
    case 1:
        document.write("Monday");
    case 2:
        document.write("Tuesday");
    case 3:
        document.write("Wednesday");
    case 4:
        document.write("Thursday");
    case 5:
        document.write("Friday");
    case 6:
        document.write("Saturday");

}