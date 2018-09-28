import std.stdio;

void fizzBuzz()
{
    for (auto i = 1; i <= 100; ++i) {
        if (i % 15 == 0) {
            writeln("FizzBazz!");
        } else if (i%5 == 0) {
            writeln("Buzz!");
        } else if (i%3 == 0) {
            writeln("Fizz!");
        } else {
            writeln(i);
        }
    }
}

void main()
{
    fizzBuzz();
}