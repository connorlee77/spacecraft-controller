function [output] = plant(u, theta)
    l = 1;
    b = 1; 
    m = 1;
    I = 1;
    
    H = [
        -1 -1 0 0 1 1 0 0; 
        0 0 -1 -1 0 0 1 1;
        -l l -b b -l l -b b];

    T = [
        cos(theta)/m, sin(theta)/m, 0;
        -sin(theta)/m, cos(theta)/m, 0;
        0, 0, 2*I];
    
    F = H'*inv(H*H')*inv(T)*u;
    
    output = T*H*F;
end