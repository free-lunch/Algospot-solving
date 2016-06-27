#include <iostream>
#include <queue>
#include <cstring>
#include <cmath>
#include <sstream>

using namespace std;

const int MAX_DISCS =  12;
int c[1<<(MAX_DISCS*2)];

int get(int state, int index) {
    return (state >> ( index *2)) & 3;
}

int set(int state, int index, int value) {
    return value << (index*2) | (state & ~(3 << (index*2)));
}

int inc(int x) {
    if(x < 0)
        return x-1;
    else
        return x+1;
}

int sgn(int x) {
    if(!x)
        return 0;
    return x> 0? 1: -1;
}

int solve(int discs, int begin) {
    int end = 0;
    for(int i=0; i< discs; ++i) {
        end = set(end, i, 3);
    }

    if(end == begin)
        return 0;

    queue<int> q;
    memset(c,0,sizeof(c));

    q.push(begin);
    q.push(end);
    c[begin] = 1;
    c[end] = -1;

    while (!q.empty()){
        int parent = q.front();
        q.pop();
        int top[4] = {-1,-1,-1,-1};
        for (int i = discs-1; i >= 0; i--) {
            top[get(parent,i)] = i;
        }


        for(int i =0; i< 4; i++){
            if(top[i] != -1) {
                for(int j = 0; j<4; j++) {
                    if (i == j)
                        continue;

                    if (top[j] == -1 || top[i] < top[j] ) {
                        int child = set(parent,top[i],j);
                        if(c[child] == 0) {
                            q.push(child);
                            c[child] = inc(c[parent]);
                        }
                        else if (c[child] * c[parent] < 0){
                            return abs(c[child]) + abs(c[parent]) -1;
                        }

                    }
                }
            }
        }
    }

    return -1;

}

int main(){
    int cases;
    cin >> cases;
    while(cases--) {
        int discs = 0, begin = 0;
        cin >> discs;
        cin.get();
        for (int i =0; i < 4; i++) {
            string s;
            int n = 0;

            getline(cin, s);
            stringstream ss(s);

            ss >> n;
            while (ss >> n) {
                begin = set(begin, n-1, i);
            }
        }

        cout<<solve(discs, begin)<<endl;
    }

    return 0;
}
