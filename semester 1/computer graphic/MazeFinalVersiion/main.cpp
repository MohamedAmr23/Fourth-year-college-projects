#define STB_IMAGE_IMPLEMENTATION

#include<iostream>
#include<cmath>
#include<Windows.h>
#include<GL/glut>
#include <GL/stb_image.h>
#include <time.h>

bool fullScreen = true;

int levels = 4,
	x, y,
	ch = -1,
	count,
	aspect,
	n = 15, m = 21,
	coinit[4][4] = {
		{ 9, 0, 0, 12 } ,
		{11 , 0, 8, 20 },
		{ 0, 2, 14, 9 },
		{ 14, 5, 14, 7 } },


	co[4][4] = {
		{ 9, 0, 0, 12 } ,
		{11 , 0, 8, 20 },
		{ 0, 2, 14, 9 },
		{ 14, 5, 14, 7 } },

	current_level = 0;

unsigned char* data = NULL;

int width, height, nrChannels;

clock_t start, endd;

char t[2];

unsigned int texture;

int maze[4][15][21] = {

{ 
{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 },
{ 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1 },
{ 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1 },
{ 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 },
{ 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1 },
{ 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1 },
{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 } },


{ { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
{ 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1 },
{ 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1 },
{ 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0 },
{ 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1 },
{ 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 },
{ 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1 },
{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 } } ,


{ { 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
{ 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1 },
{ 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1 },
{ 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1 },
{ 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1 },
{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 } },


{ { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
{ 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1 },
{ 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1 },
{ 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1 },
{ 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
{ 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1 },
{ 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 } } ,

};

bool valid(int x, int y) {
	return x >= 0 && x < n && y >= 0 && y < m;
}

void currentPoint()
{

	int sz = 5, addx = -180 + 15 * co[current_level][1], addy = 100 - co[current_level][0] * 15;

	std::cout << " Y = " << co[current_level][0] << "   -----   " << " X = " << co[current_level][1] << " ch = " << ch << "\n";

	glBegin(GL_QUADS);

	 //back
	glColor3f(.3, .3, .3);
	glVertex3f(sz + addx, sz + addy, -sz);
	glVertex3f(-sz + addx, sz + addy, -sz);
	glVertex3f(-sz + addx, sz + addy, sz);
	glVertex3f(sz + addx, sz + addy, sz);

	// front
	glColor3f(1, .3, .3);
	glVertex3f(sz + addx, -sz + addy, -sz);
	glVertex3f(-sz + addx, -sz + addy, -sz);
	glVertex3f(-sz + addx, -sz + addy, sz);
	glVertex3f(sz + addx, -sz + addy, sz);

	 //right
	glColor3f(1, .3, .3);
	glVertex3f(sz + addx, sz + addy, -sz);
	glVertex3f(sz + addx, -sz + addy, -sz);
	glVertex3f(sz + addx, -sz + addy, sz);
	glVertex3f(sz + addx, sz + addy, sz);

	// left
	glColor3f(1, .5, .5);
	glVertex3f(-sz + addx, sz + addy, -sz);
	glVertex3f(-sz + addx, -sz + addy, -sz);
	glVertex3f(-sz + addx, -sz + addy, sz);
	glVertex3f(-sz + addx, sz + addy, sz);

	// top
	glColor3f(1, .9, .9);
	glVertex3f(sz + addx, sz + addy, -sz);
	glVertex3f(-sz + addx, sz + addy, -sz);
	glVertex3f(-sz + addx, -sz + addy, -sz);
	glVertex3f(sz + addx, -sz + addy, -sz);

	// bottom
	glColor3f(1, .9, .9);
	glVertex3f(sz + addx, sz + addy, sz);
	glVertex3f(-sz + addx, sz + addy, sz);
	glVertex3f(-sz + addx, -sz + addy, sz);
	glVertex3f(sz + addx, -sz + addy, sz);
	glEnd();
}

void wallPoint(float x, float y)
{
	int sz = 7, addx = x, addy = y;

	glBegin(GL_QUADS);
	glColor3f(.3, .3, .3);

	glTexCoord2d(0.0f,0.0f);
	glVertex3f(sz + addx, sz + addy, -sz);
	glTexCoord2d(1.0f,0.0f);
	glVertex3f(-sz + addx, sz + addy, -sz);
	glTexCoord2d(1.0f,1.0f);
	glVertex3f(-sz + addx, sz + addy, sz);
	glTexCoord2d(0.0f,1.0f);
	glVertex3f(sz + addx, sz + addy, sz);

	// bottom
	glColor3f(.3, .3, .3);
	glTexCoord2d(0.0f,0.0f);
	glVertex3f(sz + addx, -sz + addy, -sz);
	glTexCoord2d(1.0f,0.0f);
	glVertex3f(-sz + addx, -sz + addy, -sz);
	glTexCoord2d(1.0f,1.0f);
	glVertex3f(-sz + addx, -sz + addy, sz);
	glTexCoord2d(0.0f,1.0f);
	glVertex3f(sz + addx, -sz + addy, sz);

	// right
	glColor3f(.5, .5, .5);
	glTexCoord2d(0.0f,0.0f);
	glVertex3f(sz + addx, sz + addy, -sz);
	glTexCoord2d(1.0f,0.0f);
	glVertex3f(sz + addx, -sz + addy, -sz);
	glTexCoord2d(1.0f,1.0f);
	glVertex3f(sz + addx, -sz + addy, sz);
	glTexCoord2d(0.0f,1.0f);
	glVertex3f(sz + addx, sz + addy, sz);

	// left
	glColor3f(.5, .5, .5);
	glTexCoord2d(0.0f,0.0f);
	glVertex3f(-sz + addx, sz + addy, -sz);
	glTexCoord2d(01.0f,0.0f);
	glVertex3f(-sz + addx, -sz + addy, -sz);
	glTexCoord2d(01.0f,1.0f);
	glVertex3f(-sz + addx, -sz + addy, sz);
	glTexCoord2d(0.0f,1.0f);
	glVertex3f(-sz + addx, sz + addy, sz);

	// back
	glColor3f(.9, .9, .9);
	glTexCoord2d(0.0f,0.0f);
	glVertex3f(sz + addx, sz + addy, -sz);
	glTexCoord2d(1.0f,0.0f);
	glVertex3f(-sz + addx, sz + addy, -sz);
	glTexCoord2d(1.0f,1.0f);
	glVertex3f(-sz + addx, -sz + addy, -sz);
	glTexCoord2d(0.0f,1.0f);
	glVertex3f(sz + addx, -sz + addy, -sz);

	//front
	glColor3f(.9, .9, .9);
	glTexCoord2d(0.0f,0.0f);
	glVertex3f(sz + addx, sz + addy, sz);
	glTexCoord2d(1.0f,0.0f);
	glVertex3f(-sz + addx, sz + addy, sz);
	glTexCoord2d(1.0f,1.0f);
	glVertex3f(-sz + addx, -sz + addy, sz);
	glTexCoord2d(0.0f,1.0f);
	glVertex3f(sz + addx, -sz + addy, sz);
	glEnd();

}

void writeStr(int x, int y, const char* str, void* font)
{

	int len = strlen(str);
	glRasterPos2f(x, y);
	for (int i = 0; i < len; i++)
	{
		glutBitmapCharacter(font, str[i]);
	}
}

void check(unsigned char* data) {
	if (data != NULL)
	{
		glGenTextures(1, &texture);
		glBindTexture(GL_TEXTURE_2D, texture);
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);

		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	}
	else
	{
		std::cout << "Failed to load texture" << std::endl;
	}
	stbi_image_free(data);
}

void load(int imgnum) {
	if (imgnum == 1) {

		data = stbi_load("wall.bmp", &width, &height, &nrChannels, 0);
		check(data);
	}
	else if (imgnum == 2) {

		data = stbi_load("images.jpeg", &width, &height, &nrChannels, 0);
		check(data);
	}
}

void keyboard(unsigned char key, int x, int y) {
	if (key == 32)
	{
		ch = 1;
		current_level = 0;
		co[current_level][0] = coinit[current_level][0];
		co[current_level][1] = coinit[current_level][1];
		start = clock();
	}

	else if (key == 13)
	{
		ch = 1;
		start = clock();
	}

	else if (key == 27)exit(0);

	else if (key == 9)ch = -1;
}

void map() {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glLoadIdentity();
	glTranslatef(0, 0, -90.0f);

	load(2);

	glColor3f(0.5, 0.5, 0.5);
	glBegin(GL_POLYGON);
	glTexCoord2f(0, 1);
	glVertex2f(-195, -120);
	glTexCoord2f(1, 1);
	glVertex2f(120, -120);
	glTexCoord2f(1, 0);
	glVertex2f(120, 115);
	glTexCoord2f(0, 0);
	glVertex2f(-195, 115);
	glEnd();



	glColor3f(0.9490196078431373, 0.9490196078431373, 0.9490196078431373);
	writeStr(-50, 130, "TIME REMAINING : ", GLUT_BITMAP_HELVETICA_18);
	glColor3f(0.9529411764705882, 0.1411764705882353, 0.1411764705882353);
	writeStr(-187, 170, "Press Tap To Go To Main Menu ", GLUT_BITMAP_HELVETICA_18);
	writeStr(-180, 140, "Press Space To Restart The Game From Level 0", GLUT_BITMAP_HELVETICA_18);
	int num = 20 - count;

	t[0] = '0' + num / 10;
	t[1] = '0' + num % 10;


	glColor3f(0.9490196078431373, 0.9490196078431373, 0.9490196078431373);
	writeStr(70, 142, t, GLUT_BITMAP_TIMES_ROMAN_24);

	load(1);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (maze[current_level][i][j]) {
				wallPoint(-180 + j* 15, 100 - i * 15);
			}
		}
	}

	currentPoint();

	glutSwapBuffers();
}

void background() {

	glClearColor(0.2, 0.2, 0.2, 1);
	glColor3f(0.2, 0.2, 0.2);

	glEnable(GL_DEPTH_TEST);
	glEnable(GL_TEXTURE_2D);

}

void cover() {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glLoadIdentity();
	glTranslatef(0, 0, -100.0f);
	background();

	glColor3f(0.7764705882352941, 0.607843137254902, 0.4823529411764706);
	writeStr(-50, 90, "\"THE MAZE\"", GLUT_BITMAP_TIMES_ROMAN_24);
	writeStr(-190, -105, "Made By: ", GLUT_BITMAP_TIMES_ROMAN_24);

	glColor3f(0.67, 0.4, 0.8);
	writeStr(-203, -120, "1-Ahmed Osama Fawzy", GLUT_BITMAP_TIMES_ROMAN_24);
	writeStr(-198, -130, "2-Ahmed Samy Ahmed", GLUT_BITMAP_TIMES_ROMAN_24);
	writeStr(-194, -140, "3-Nada Magdy AbdElazim", GLUT_BITMAP_TIMES_ROMAN_24);

	glColor3f(0.7764705882352941, 0.607843137254902, 0.4823529411764706);
	writeStr(-80, -10, "If you want to start the game press space", GLUT_BITMAP_TIMES_ROMAN_24);
	writeStr(-80, -30, "If you want to close the game press esc", GLUT_BITMAP_TIMES_ROMAN_24);
	glutSwapBuffers();

}

void winScreen() {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glLoadIdentity();
	glTranslatef(0, 0, -50);
	glColor3f(0, 1, 0);
	writeStr(-25, 40, "WILL DONE", GLUT_BITMAP_TIMES_ROMAN_24);

	glColor3f(0.7764705882352941, 0.607843137254902, 0.4823529411764706);
	writeStr(-50, -20, "If you want to end the game ,press tap ", GLUT_BITMAP_TIMES_ROMAN_24);
	writeStr(-50, -60, "If you want to next level ,press enter ", GLUT_BITMAP_TIMES_ROMAN_24);
	writeStr(-50, -40, "If you want to play again , press space", GLUT_BITMAP_TIMES_ROMAN_24);
	glutSwapBuffers();
}

void loseScreen() {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glLoadIdentity();
	glTranslatef(0, 0, -50.0f);
	glColor3f(0.7764705882352941, 0.607843137254902, 0.4823529411764706);
	writeStr(-50, 20, "TIME OUT ", GLUT_BITMAP_TIMES_ROMAN_24);
	background();


	glColor3f(0.7764705882352941, 0.607843137254902, 0.4823529411764706);
	writeStr(-50, -20, "If you want to end the game ,press tap", GLUT_BITMAP_TIMES_ROMAN_24);
	writeStr(-50, -40, "If you want to play again, press space", GLUT_BITMAP_TIMES_ROMAN_24);
	glutSwapBuffers();
}

void FinshScreen() {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glLoadIdentity();
	glTranslatef(0, 0, -50);
	glColor3f(0, 1, 0);
	writeStr(-50, 50, "CONGRATULATIONS!", GLUT_BITMAP_TIMES_ROMAN_24);
	writeStr(-50, 30, "You have Finshed the maze", GLUT_BITMAP_TIMES_ROMAN_24);
	glColor3f(1.0, 1.0, 1.0);
	writeStr(-50, 10, "Press space to restart the game ", GLUT_BITMAP_TIMES_ROMAN_24);
	writeStr(-50, 0, "Press tap to go to main menu", GLUT_BITMAP_TIMES_ROMAN_24);
	glutSwapBuffers();
}

void display() {
	if (ch == -1)cover();
	else if (ch == 1) {
		map();
	}
	else if (ch == 2) {
		loseScreen();
	}

	if (co[current_level][0] == co[current_level][2] && co[current_level][1] == co[current_level][3]) {


		if (current_level == levels - 1) {
			current_level = 0;
			FinshScreen();
		}
		else
		{

			co[current_level][0] = coinit[current_level][0];
			co[current_level][1] = coinit[current_level][1];
			current_level++;
			winScreen();
		}

		ch = 3;
	}

	if (ch != 1) {
		co[current_level][0] = coinit[current_level][0];
		co[current_level][1] = coinit[current_level][1];
	}

}

void SpecialKey(int key, int x, int y) {
	switch (key)
	{
	case GLUT_KEY_UP:
		if (valid(co[current_level][0] - 1, co[current_level][1]) && !maze[current_level][co[current_level][0] - 1][co[current_level][1]])
			co[current_level][0]--;
		break;
	case GLUT_KEY_DOWN:
		if (valid(co[current_level][0] + 1, co[current_level][1]) && !maze[current_level][co[current_level][0] + 1][co[current_level][1]])
			co[current_level][0]++;
		break;
	case GLUT_KEY_LEFT:
		if (valid(co[current_level][0], co[current_level][1] - 1) && !maze[current_level][co[current_level][0]][co[current_level][1] - 1])
			co[current_level][1]--;
		break;
	case GLUT_KEY_RIGHT:
		if (valid(co[current_level][0], co[current_level][1] + 1) && !maze[current_level][co[current_level][0]][co[current_level][1] + 1])
			co[current_level][1]++;
		break;
	}

	if( key == GLUT_KEY_F1){
		fullScreen = !fullScreen;
		if(fullScreen)
			glutFullScreen();
		else{
			glutPositionWindow(15,15);
			glutReshapeWindow(1200,600);
		}
	}
	display();
}

void reshape(GLsizei width, GLsizei height) {
	if (height == 0) height = 1;
	GLfloat aspect = (GLfloat)width / (GLfloat)height;
	glViewport(0, 0, width, height);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(100, aspect, 0.7f, 200.0f);

	gluLookAt(0, -60, 50, 20, 0, -180, 0, 10, 1);

	glMatrixMode(GL_MODELVIEW);

}

void idle()
{
	if (ch == 1)
	{
		endd = clock();
		/*std::cout<<endd<<std::endl;*/
		count = (endd - start) / CLOCKS_PER_SEC;
		if (count == 20) {
			ch = 2;
		}
	}
	glutPostRedisplay();
}

int main(int agrc, char** agrv) {
	glutInit(&agrc, agrv);
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE);
	int width = GetSystemMetrics(SM_CXSCREEN);
	int height = GetSystemMetrics(SM_CYSCREEN);
	glutInitWindowSize(width, height);
	glutCreateWindow("Solve The Maze");
	glEnable(GL_DEPTH_TEST);
	glutIdleFunc(idle);
	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutSpecialFunc(SpecialKey);
	glutKeyboardFunc(keyboard);
	glutMainLoop();
	system("pause");
	return 0;
}
