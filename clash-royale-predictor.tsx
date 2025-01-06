import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import { Loader2 } from 'lucide-react';

const MatchPredictor = () => {
  const [playerTag, setPlayerTag] = useState('');
  const [predictions, setPredictions] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeBattles = (tag) => {
    setLoading(true);
    // Simulate API call - replace with actual API
    setTimeout(() => {
      const mockData = {
        winRate: 65,
        recentBattles: [
          { opponent: "Player1", deck: "Golem Beat", winChance: 70 },
          { opponent: "Player2", deck: "Log Bait", winChance: 45 },
          { opponent: "Player3", deck: "Lava Hound", winChance: 80 }
        ],
        performanceData: [
          { battle: 1, winRate: 60 },
          { battle: 2, winRate: 65 },
          { battle: 3, winRate: 55 },
          { battle: 4, winRate: 70 },
          { battle: 5, winRate: 65 }
        ]
      };
      setPredictions(mockData);
      setLoading(false);
    }, 1000);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 to-purple-900 p-4">
      <Card className="max-w-4xl mx-auto bg-white/95 backdrop-blur">
        <CardHeader>
          <CardTitle className="text-2xl text-center font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            Clash Royale Match Predictor
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-6">
          <div className="flex gap-2">
            <Input
              placeholder="#Player Tag"
              value={playerTag}
              onChange={(e) => setPlayerTag(e.target.value)}
              className="flex-1"
            />
            <Button 
              onClick={() => analyzeBattles(playerTag)}
              disabled={loading || !playerTag}
              className="bg-gradient-to-r from-blue-500 to-purple-500"
            >
              {loading ? <Loader2 className="animate-spin" /> : 'Analyze'}
            </Button>
          </div>

          {predictions && (
            <div className="space-y-6">
              <div className="text-center p-4 bg-gradient-to-r from-blue-100 to-purple-100 rounded-lg">
                <span className="text-3xl font-bold text-blue-800">
                  {predictions.winRate}%
                </span>
                <p className="text-sm text-gray-600">Overall Win Rate</p>
              </div>

              <div className="h-64 w-full">
                <ResponsiveContainer>
                  <LineChart data={predictions.performanceData}>
                    <XAxis dataKey="battle" />
                    <YAxis domain={[0, 100]} />
                    <Tooltip />
                    <Line 
                      type="monotone" 
                      dataKey="winRate" 
                      stroke="#4F46E5"
                      strokeWidth={2}
                    />
                  </LineChart>
                </ResponsiveContainer>
              </div>

              <div className="space-y-2">
                {predictions.recentBattles.map((battle, index) => (
                  <div 
                    key={index}
                    className="p-4 rounded-lg bg-gradient-to-r from-blue-50 to-purple-50 flex justify-between items-center"
                  >
                    <div>
                      <p className="font-semibold">{battle.opponent}</p>
                      <p className="text-sm text-gray-600">{battle.deck}</p>
                    </div>
                    <div className="text-right">
                      <p className="text-2xl font-bold text-blue-600">
                        {battle.winChance}%
                      </p>
                      <p className="text-sm text-gray-600">Win Chance</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

export default MatchPredictor;
