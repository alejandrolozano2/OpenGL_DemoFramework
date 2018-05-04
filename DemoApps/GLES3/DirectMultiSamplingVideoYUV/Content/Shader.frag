#version 300 es
#ifdef GL_FRAGMENT_PRECISION_HIGH
 precision highp float;
#else
 precision mediump float;
 #endif
 
 uniform sampler2D my_Texture0;           
 uniform sampler2D my_Texture1;
 in vec2 vTexcoor;

layout(location = 0) out vec2 out_color;
layout(location = 1) out vec2 out_color2;

 void main()
 {  

    
    /*Downsample CbCr*/
    float ycoordinate = vTexcoor.y * 2.0;


    float Y1;
    float Y2;
    float Cb;
    float Cr;
    vec2 mycoord = vec2(vTexcoor.x, ycoordinate); 

  
    Y1 = texture(my_Texture0, vTexcoor).x;
    Y2 = texture(my_Texture0, vTexcoor).z;
    
    Cb = texture(my_Texture0, mycoord).y;
    Cr = texture(my_Texture0, mycoord).a;

    out_color =vec2(Y1,Y2);
    out_color2 =vec2(Cb,Cr); 

 }

