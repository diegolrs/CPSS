#pragma once
#include <string>

class Material
{
	public:
       Material();
       Material(std::string name);
       Material(std::string name, int id);
       Material();
    private:
        std::string name;
        int id;
	public:
};