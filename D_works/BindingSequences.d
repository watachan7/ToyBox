import std.stdio;

void main() {
    int[] intString1 = [1, 2, 3];
    int[] intString2 = [4, 5, 6];
    int[] results = intString1 ~ intString2;
    results ~= 7;
    results ~= [8, 9];
    writeln(results);
}