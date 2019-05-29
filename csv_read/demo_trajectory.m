%{
Assignment: Demo Trajectory
Course: Ae 105C
Author: Parker Brown
Date: 5/30/2019
%}
clear; close all; clc;

%% Import Demo Trajectory

load Positions.csv

t = Positions(:,1);
x1 = Positions(:,2);
y1 = Positions(:,3);
x2 = Positions(:,4);
y2 = Positions(:,5);

collisions = any(vecnorm([x1,y1]-[x2,y2],2,2) - 2*norm([0.2, 0.2]) < 0)
closest = min(vecnorm([x1,y1]-[x2,y2],2,2) - 2*norm([0.2, 0.2]))

% Plot Trajectory
fig1 = figure(1);
hold on;
plot(x1,y1,'b');
plot(x2,y2,'r');
grid on;
axis equal;

title('Demo Trajectory')
xlabel('x [m]')
ylabel('y [m]')
legend('S/C 1', 'S/C 2')

saveas(fig1,'traj.png')

% Plot Trajectory vs Time
fig2 = figure(2);
sgtitle('Demo Trajectory')
subplot(4,1,1);
plot(t/3600,x1,'b');
ylabel('x_1(t)');
axis tight;
subplot(4,1,2);
plot(t/3600,y1,'b');
ylabel('y_1(t)');
axis tight;
subplot(4,1,3);
plot(t/3600,x2,'r');
ylabel('x_2(t)');
axis tight;
subplot(4,1,4);
plot(t/3600,y2,'r');
ylabel('y_2(t)');
xlabel('Time [hours]')
axis tight;

saveas(fig2,'trajvtime.png')