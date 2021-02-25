#include <bits/stdc++.h>
#ifdef ONLINE_JUDGE
#define endl "\n"
#endif
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    const char *file = "a.txt";
    freopen("../problem/a.txt", "r", stdin);
    int D, I, S, V, F;
    cin >> D >> I >> S >> V >> F;
    vector<int> B(S), E(S), L(S);
    vector<string> streets(S);
    map<string, int> street_map;
    for (int i = 0; i < S; i++)
    {
        cin >> B[i] >> E[i];
        cin >> streets[i];
        street_map[streets[i]] = i;
        cin >> L[i];
    }
    vector<vector<int>> cars(V);
    for (int i = 0; i < V; i++)
    {
        int P;
        cin >> P;
        for (int j = 0; j < P; j++)
        {
            string ss;
            cin >> ss;
            int val = street_map[ss];
            cars[i].push_back(val);
        }
    }
    // solve();

    vector<int> in_count(I, 0), out_count(I, 0);
    vector<vector<pair<int, int>>> arrival_dist(I);
    vector<map<string, int>> ans(I);

    for (int i = 0; i < V; i++)
    {
        int dist = 0;
        int cnt = 0;
        for (auto str : cars[i])
        {
            int start = B[str];
            int end = E[str];
            out_count[start]++;
            in_count[end]++;

            dist += L[str];
            if (cnt == 0)
                arrival_dist[start].push_back({i, 0});
            arrival_dist[end].push_back({i, dist});

            ans[end][streets[str]] += 1;

            cnt++;
            // cout << start << " " << end << '\n';
        }
    }

    // for (int i = 0; i < I; i++)
    // {
    //     cout << in_count[i] << " " << out_count[i] << '\n';
    // }

    cout << I << '\n';
    for (int i = 0; i < I; i++)
    {
        cout << i << '\n';

        // for (auto a : arrival_dist[i])
        // {
        //     cout << a.first << " " << a.second << '\n';
        // }
    }

    return 0;
}