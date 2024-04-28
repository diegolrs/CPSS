#pragma once
#include "Material/Metal"

class Item
{
	public:
		float value;
		int test;

	   Item(float value, Metal metal);
	public:
		float getValue();
		void setValue(float value);
		int getTest();
		void setTest(int test);
};