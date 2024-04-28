#pragma once
#include "Material/Metal"

class Item
{
	private:
		float value;
		int test;
	public:
	   Item(float value, Metal metal);
	public:
		float getValue();
		void setValue(float value);
		int getTest();
		void setTest(int test);
};