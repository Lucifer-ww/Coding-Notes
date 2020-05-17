#include <vector>
using namespace std;
class vector {
    public:
        vector<string> split(string aStr, char aDem = ' ')
        {
            vector<string> sv;
            sv.clear();
            stringstream res(aStr);
            string temp;
            while (getline(res, temp, aDem))
            {
                sv.push_back(temp);
            }
            return sv;
        }
};