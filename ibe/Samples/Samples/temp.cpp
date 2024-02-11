
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vn vector<int>
#define pb push_back
#define forn for (int i = 0; i < n; i++)
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
        int k;
        cin >> k;
        int n = (-13 + (sqrt(169 + 52 * k))) / 26;
        if (n)
        {
            int x = n * (26 + (n - 1) * 13);
            x = k - x;
            n += 1;
            if (x == 0)
            {
                cout << 'z' << endl;
                else
                {
                    int t = (x / n);
                    if (x % n)
                        t++;
                    cout << char(96 + t) << endl;
                }
            }
        }
        cout<<char(96+k)<<endl;
    }
    return 0;
}