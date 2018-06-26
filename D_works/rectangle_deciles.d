import std.random;
import std.range;
import std.stdio;
 
class Rectangle {
    double width;
    double height;
 
    this(double width, double height) {
        this.width = width;
        this.height = height;
    }
 
    double area() {
        return width * height;
    }
}
 
void main(string[] args) {
    Rectangle[] rs = new Rectangle[1_000_000];
    rs = rs.map!(x => new Rectangle(uniform(0.0, 1.0),
                                    uniform(0.0, 1.0))).array;
    rs.sort!((x, y) => x.width < y.width);
    foreach(int i; 0..10) {
        writefln("%0.4f\t%0.4f\t%0.4f",
                 rs[i * 100_000].width,
                 rs[i * 100_000].height,
                 rs[i * 100_000].area());
    }
}