#include <cstdio>
#include <iostream>
#include <vector>
#include <limits>
#include <cmath>
#include <queue>
using namespace std;

#define MAX  numeric_limits<int>::max()
typedef pair<double, int> NODE;

double solve(int N, int M, vector<vector<NODE> > adj) {
    vector<double> dist(N, 0);
    priority_queue<NODE> q;

    q.push({-1.0, 0});
    dist[0] = 1.0;

    while(!q.empty()) {
        int v1 = q.top().second;
        int cost = -q.top().first;
        q.pop();

        if(dist[v1] < cost)
            continue;

        if(v1 == N - 1)
            break;

        for(auto it = adj[v1].begin(); it != adj[v1].end(); it ++) {

            double nextDist = it->first * dist[v1];
            if(dist[it->second] == 0.0||nextDist < dist[it->second]) {
                dist[it->second] = nextDist;
                q.push({-nextDist, it->second});
            }
        }

    }
    return dist[N-1];
}

int main() {
    cin.sync_with_stdio(false);
    int tests = 0;
    cin >> tests;
    vector<vector<NODE> > adj;
    while(tests--) {
        int N, M;
        cin >> N >> M;

        adj.clear();
        adj.resize(N+1);

        for(int i = 0; i < M; i++) {
            int v1, v2;
            double value;

            scanf("%d %d %lf", &v1, &v2, &value);

            adj[v1].push_back({value, v2});
            adj[v2].push_back({value, v1});
        }

        cout.setf(ios::showpoint);
        cout.precision(10);
        cout << solve(N, M, adj) << endl;

    };
    return 0;
}
