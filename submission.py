# Example of SQL query
query_example = """
                SELECT mascot
                FROM `bigquery-public-data.ncaa_basketball.mascots`
                WHERE market = 'Georgia Tech'
                """

#### YOUR CODE GOES BELOW HERE  #####

#(1)
query_1 = """
            (SELECT DISTINCT P.id, P.name
            FROM `cs4400_ncaa_basketball.player_game` as PGAME, `cs4400_ncaa_basketball.player` as P, `cs4400_ncaa_basketball.game` as GAME
            WHERE GAME.season = 2013 AND GAME.id = PGAME.game_id AND PGAME.player_id = P.id)

            INTERSECT DISTINCT

            (SELECT DISTINCT P.id, P.name
            FROM `cs4400_ncaa_basketball.player_game` as PGAME, `cs4400_ncaa_basketball.player` as P, `cs4400_ncaa_basketball.game` as GAME
            WHERE GAME.season = 2017 AND GAME.id = PGAME.game_id AND PGAME.player_id = P.id)

            ORDER BY name
          """

#(2)
query_2 = """
            SELECT DISTINCT P.id, P.name
            FROM `cs4400_ncaa_basketball.player_game` as PGAME, `cs4400_ncaa_basketball.player` as P, `cs4400_ncaa_basketball.game` as GAME
            WHERE PGAME.player_id = P.id AND PGAME.game_id = GAME.id
            GROUP BY P.id, P.name, GAME.season
            HAVING COUNT(*) >= 40

            ORDER BY name
          """

#(3)
query_3 = """
            SELECT DISTINCT P.id, P.name
            FROM `cs4400_ncaa_basketball.player` as P JOIN `cs4400_ncaa_basketball.player_game` as PGAME ON P.id = PGAME.player_id
            WHERE PGAME.points > 10 AND PGAME.points IS NOT NULL
            GROUP BY P.id, P.name
            HAVING COUNT(P.name) >= 10


            ORDER BY name

          """

#(4)
query_4 = """
          YOUR QUERY HERE
          """

#(5)
query_5 = """
          SELECT DISTINCT PG1.player_id, PG2.player_id, AVG(partner_score)
          FROM `cs4400_ncaa_basketball.player_game` as PG
          WHERE PG.player_id IN (SELECT PG1.player_id, PG2.player_id, PG1.points - PG2.points as partner_score
                                         FROM `cs4400_ncaa_basketball.game` as G, 
                                         `cs4400_ncaa_basketball.player_game` as PG1 INNER JOIN 
                                         `cs4400_ncaa_basketball.player_game` as PG2 ON PG1.player_id <> PG2.player_id 
                                         WHERE PG1.points IS NOT NULL and
                                         PG2.points IS NOT NULL 
                                         and PG1.game_id = PG2.game_id and PG1.team_id = PG2.team_id 
                                         and G.season = 2017)
            GROUP BY COUNT()
          """

#(6)
query_6 = """
          YOUR QUERY HERE
          """

#(7)
query_7 = """
          YOUR QUERY HERE
          """

#(8)
query_8 = """
          YOUR QUERY HERE
          """

#(9)
query_9 = """
            SELECT DISTINCT T.name, T.school
            FROM `cs4400_ncaa_basketball.team` as T, `cs4400_ncaa_basketball.player_game` as PGAME, `sodium-carver-343723.cs4400_ncaa_basketball.team_game` as TG,  `cs4400_ncaa_basketball.game` as GAME
            WHERE GAME.season = 2017 and PGAME.team_id = T.id AND GAME.id = PGAME.game_id
            GROUP BY T.name, T.school, PGAME.points
            HAVING COUNT(PGAME.points) > 0

            ORDER BY T.name
          """

#(10)
query_10 = """
           YOUR QUERY HERE
           """

#### YOUR CODE GOES ABOVE HERE  #####
