#include <iostream>
#include <map>
#include <list>
#include "./json.hpp"

using namespace nlohmann;
using std::string;
using std::map;

void print(std::string newString) {
    // If you want to complain about this you can kindly fuck off
    std::cout << newString << "\n";
}

class World {
    public:
        int getMonth() {
            return calendar["month"];
        }

        void setMonth(int newMonth) {
            calendar["month"] = newMonth;
        }

        int getYear() {
            return calendar["year"];
        }

        void setYear(int newYear) {
            calendar["year"] = newYear;
        }

        std::string getDate() {
            return std::to_string(calendar["month"]) + "." + std::to_string(calendar["year"]); // This simple trick is HATED by Rust programmers! Just add three strings together.
        }

        void setWorldname(std::string newWorldname) {
            worldname = newWorldname;
        }

        std::string getWorldname() {
            return worldname;
        }

    private:
        std::string worldname;

		map<string, int> calendar {
			{"month", 1},
			{"year", 0}
		};

        int wealth = 50;

};

int main() {
    World w;
    
    return 0;
}