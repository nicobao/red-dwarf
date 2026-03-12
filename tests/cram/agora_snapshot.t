Agora pipeline snapshot test using small fixture data (below-100-ptpts).
Shows representative opinions, group-aware consensus, consensus statements,
and divisive statements with cross-group comparisons.

  $ cd "$TESTDIR/../.."
  $ uv run python scripts/print_agora_snapshot.py tests/fixtures/below-100-ptpts
  === AGORA PIPELINE SNAPSHOT ===
  Fixture: tests/fixtures/below-100-ptpts
  Participants: 19 clustered, 3 groups
  Statements: 42 active (2 moderated out)
  
  === REPRESENTATIVE OPINIONS ===
  
  --- Group 0 ---
   #  Sel  Dir    Stmt  Effect  Text
                                     G0 pa/pd (na/nd/ns) |  G1 pa/pd (na/nd/ns) |  G2 pa/pd (na/nd/ns)
   1  [*]  dis    s13   4.8000  "Polis statements can be too si..."
                                     0.20/0.80 ( 0/ 3/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.91/0.09 ( 9/ 0/ 9)
   2  [*]  agree  s1    4.4800  "The prominent display of divis..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.50 ( 0/ 2/ 4) |  0.20/0.40 ( 1/ 3/ 8)
   3  [ ]  dis    s29   3.5556  "whether I engage through a tex..."
                                     0.33/0.67 ( 0/ 1/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.17/0.17 ( 0/ 0/ 4)
   4  [ ]  dis    s34   3.5556  "It asks for my email once I’ve..."
                                     0.33/0.67 ( 0/ 1/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.67/0.17 ( 3/ 0/ 4)
   5  [*]  dis    s9    3.4133  "Due to the 140 character limit..."
                                     0.20/0.80 ( 0/ 3/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.67/0.17 ( 7/ 1/10)
   6  [*]  dis    s20   3.2000  "It's hard to communicate techn..."
                                     0.20/0.80 ( 0/ 3/ 3) |  0.33/0.17 ( 1/ 0/ 4) |  0.73/0.27 ( 7/ 2/ 9)
   7  [ ]  dis    s27   2.7500  "I wish statements weren't limi..."
                                     0.25/0.50 ( 0/ 1/ 2) |  0.20/0.20 ( 0/ 0/ 3) |  0.75/0.12 ( 5/ 0/ 6)
   8  [ ]  dis    s35   2.6667  "Set a slightly higher characte..."
                                     0.33/0.67 ( 0/ 1/ 1) |  0.33/0.33 ( 0/ 0/ 1) |  0.60/0.20 ( 2/ 0/ 3)
   9  [ ]  agree  s22   1.8000  "Polis relies on the participan..."
                                     0.60/0.40 ( 2/ 1/ 3) |  0.33/0.33 ( 1/ 1/ 4) |  0.18/0.73 ( 1/ 7/ 9)
  10  [ ]  agree  s8    1.7920  "Polis needs a way to showcase ..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.50/0.20 ( 4/ 1/ 8)
  11  [ ]  agree  s5    1.7920  "Tooling for multiple moderator..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.50/0.10 ( 4/ 0/ 8)
  12  [ ]  dis    s19   1.5300  "Polis feels too abstract and a..."
                                     0.40/0.60 ( 1/ 2/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.77/0.23 ( 9/ 2/11)
  13  [ ]  agree  s24   1.2800  "Polis needs to support transla..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.70/0.10 ( 6/ 0/ 8)
  14  [ ]  agree  s16   1.2800  "It sucks that there's no way t..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.33/0.17 ( 1/ 0/ 4) |  0.58/0.25 ( 6/ 2/10)
  15  [ ]  agree  s4    1.2000  "There's no way to review previ..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.73/0.27 ( 7/ 2/ 9)
  16  [ ]  dis    s15   1.2000  "The inability to search for st..."
                                     0.40/0.40 ( 1/ 1/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.45/0.18 ( 4/ 1/ 9)
  17  [ ]  dis    s17   1.2000  "I have no way to communicate t..."
                                     0.20/0.40 ( 0/ 1/ 3) |  0.29/0.29 ( 1/ 1/ 5) |  0.70/0.10 ( 6/ 0/ 8)
  18  [ ]  agree  s23   1.1667  "There can be a bias against mi..."
                                     0.50/0.50 ( 1/ 1/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.30/0.20 ( 2/ 1/ 8)
  19  [ ]  agree  s14   1.1250  "Polis should have a "remind me..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.17/0.50 ( 0/ 2/ 4) |  0.67/0.08 ( 7/ 0/10)
  20  [ ]  agree  s31   1.1250  "Nuance in Polis is created by ..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.50/0.25 ( 1/ 0/ 2) |  0.50/0.25 ( 1/ 0/ 2)
  21  [ ]  dis    s25   1.0080  "I want to be able to make a st..."
                                     0.40/0.60 ( 1/ 2/ 3) |  0.17/0.50 ( 0/ 2/ 4) |  0.60/0.30 ( 5/ 2/ 8)
  22  [ ]  agree  s18   0.9844  "I am worried bad actors can sw..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.33/0.17 ( 1/ 0/ 4) |  0.70/0.20 ( 6/ 1/ 8)
  23  [ ]  dis    s21   0.9167  "I want to be able to share mor..."
                                     0.50/0.50 ( 1/ 1/ 2) |  0.20/0.60 ( 0/ 2/ 3) |  0.75/0.12 ( 5/ 0/ 6)
  24  [ ]  agree  s7    0.8750  "The Polis website is not compl..."
                                     0.50/0.25 ( 1/ 0/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.40/0.20 ( 3/ 1/ 8)
  25  [ ]  dis    s2    0.8750  "There's no way to differentiat..."
                                     0.25/0.50 ( 0/ 1/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.60/0.30 ( 5/ 2/ 8)
  26  [ ]  agree  s12   0.8750  "Polis is a very simple tool to..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.67/0.17 ( 3/ 0/ 4) |  0.60/0.20 ( 5/ 1/ 8)
  27  [ ]  agree  s30   0.8438  "Polis statements are atomic/bi..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.67/0.33 ( 1/ 0/ 1) |  0.60/0.20 ( 2/ 0/ 3)
  28  [ ]  dis    s0    0.7875  "Polis is perfect just the way ..."
                                     0.25/0.75 ( 0/ 2/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.10/0.90 ( 0/ 8/ 8)
  29  [ ]  agree  s26   0.7564  "I like how Polis relies on use..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.83/0.17 ( 4/ 0/ 4) |  0.78/0.11 ( 6/ 0/ 7)
  30  [ ]  dis    s37   0.7500  "Admin option of setting a thre..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.67/0.33 ( 1/ 0/ 1)
  31  [ ]  agree  s10   0.7467  "Comments should follow a narra..."
                                     0.40/0.40 ( 1/ 1/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.30/0.30 ( 2/ 2/ 8)
  32  [ ]  agree  s6    0.7200  "It's unclear if Polis' algorit..."
                                     0.60/0.20 ( 2/ 0/ 3) |  0.29/0.43 ( 1/ 2/ 5) |  0.64/0.09 ( 6/ 0/ 9)
  33  [ ]  agree  s32   0.6667  "There should be a QR code for ..."
                                     0.67/0.33 ( 1/ 0/ 1) |  0.75/0.25 ( 2/ 0/ 2) |  0.50/0.25 ( 1/ 0/ 2)
  34  [ ]  agree  s36   0.6667  "Give participants feedback abo..."
                                     0.67/0.33 ( 1/ 0/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.75/0.25 ( 2/ 0/ 2)
  35  [ ]  agree  s38   0.6222  "Fix log in"
                                     0.67/0.33 ( 1/ 0/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.80/0.20 ( 3/ 0/ 3)
  36  [ ]  agree  s28   0.6188  "Questions that have been 'pass..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.75/0.25 ( 2/ 0/ 2) |  0.89/0.11 ( 7/ 0/ 7)
  37  [ ]  agree  s3    0.5833  "Polis user-facing documentatio..."
                                     0.50/0.25 ( 1/ 0/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.60/0.10 ( 5/ 0/ 8)
  38  [ ]  agree  s42   0.5000  "There is no clear visual hiera..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  39  [ ]  agree  s39   0.5000  "testing if this works when i s..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  40  [ ]  agree  s40   0.5000  "Testing out screen reader to s..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  41  [ ]  agree  s41   0.5000  "the interface is lack of space..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  42  [ ]  agree  s43   0.5000  "test"
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  
  --- Group 1 ---
   #  Sel  Dir    Stmt  Effect  Text
                                     G0 pa/pd (na/nd/ns) |  G1 pa/pd (na/nd/ns) |  G2 pa/pd (na/nd/ns)
   1  [ ]  dis    s14   3.5000  "Polis should have a "remind me..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.17/0.50 ( 0/ 2/ 4) |  0.67/0.08 ( 7/ 0/10)
   2  [ ]  dis    s6    2.5714  "It's unclear if Polis' algorit..."
                                     0.60/0.20 ( 2/ 0/ 3) |  0.29/0.43 ( 1/ 2/ 5) |  0.64/0.09 ( 6/ 0/ 9)
   3  [ ]  dis    s21   1.8000  "I want to be able to share mor..."
                                     0.50/0.50 ( 1/ 1/ 2) |  0.20/0.60 ( 0/ 2/ 3) |  0.75/0.12 ( 5/ 0/ 6)
   4  [ ]  agree  s29   1.7500  "whether I engage through a tex..."
                                     0.33/0.67 ( 0/ 1/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.17/0.17 ( 0/ 0/ 4)
   5  [ ]  dis    s3    1.3333  "Polis user-facing documentatio..."
                                     0.50/0.25 ( 1/ 0/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.60/0.10 ( 5/ 0/ 8)
   6  [ ]  agree  s32   0.9375  "There should be a QR code for ..."
                                     0.67/0.33 ( 1/ 0/ 1) |  0.75/0.25 ( 2/ 0/ 2) |  0.50/0.25 ( 1/ 0/ 2)
   7  [ ]  agree  s26   0.8333  "I like how Polis relies on use..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.83/0.17 ( 4/ 0/ 4) |  0.78/0.11 ( 6/ 0/ 7)
   8  [ ]  dis    s1    0.8125  "The prominent display of divis..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.50 ( 0/ 2/ 4) |  0.20/0.40 ( 1/ 3/ 8)
   9  [ ]  dis    s37   0.7500  "Admin option of setting a thre..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.67/0.33 ( 1/ 0/ 1)
  10  [ ]  dis    s7    0.6667  "The Polis website is not compl..."
                                     0.50/0.25 ( 1/ 0/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.40/0.20 ( 3/ 1/ 8)
  11  [ ]  agree  s12   0.6667  "Polis is a very simple tool to..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.67/0.17 ( 3/ 0/ 4) |  0.60/0.20 ( 5/ 1/ 8)
  12  [ ]  dis    s25   0.6500  "I want to be able to make a st..."
                                     0.40/0.60 ( 1/ 2/ 3) |  0.17/0.50 ( 0/ 2/ 4) |  0.60/0.30 ( 5/ 2/ 8)
  13  [ ]  agree  s30   0.6222  "Polis statements are atomic/bi..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.67/0.33 ( 1/ 0/ 1) |  0.60/0.20 ( 2/ 0/ 3)
  14  [ ]  agree  s28   0.6188  "Questions that have been 'pass..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.75/0.25 ( 2/ 0/ 2) |  0.89/0.11 ( 7/ 0/ 7)
  15  [ ]  dis    s17   0.5306  "I have no way to communicate t..."
                                     0.20/0.40 ( 0/ 1/ 3) |  0.29/0.29 ( 1/ 1/ 5) |  0.70/0.10 ( 6/ 0/ 8)
  16  [ ]  agree  s40   0.5000  "Testing out screen reader to s..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  17  [ ]  agree  s41   0.5000  "the interface is lack of space..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  18  [ ]  agree  s39   0.5000  "testing if this works when i s..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  19  [ ]  agree  s42   0.5000  "There is no clear visual hiera..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  20  [ ]  agree  s43   0.5000  "test"
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  21  [ ]  dis    s23   0.4444  "There can be a bias against mi..."
                                     0.50/0.50 ( 1/ 1/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.30/0.20 ( 2/ 1/ 8)
  22  [ ]  agree  s34   0.4375  "It asks for my email once I’ve..."
                                     0.33/0.67 ( 0/ 1/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.67/0.17 ( 3/ 0/ 4)
  23  [ ]  agree  s22   0.3889  "Polis relies on the participan..."
                                     0.60/0.40 ( 2/ 1/ 3) |  0.33/0.33 ( 1/ 1/ 4) |  0.18/0.73 ( 1/ 7/ 9)
  24  [ ]  dis    s13   0.3889  "Polis statements can be too si..."
                                     0.20/0.80 ( 0/ 3/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.91/0.09 ( 9/ 0/ 9)
  25  [ ]  agree  s31   0.3750  "Nuance in Polis is created by ..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.50/0.25 ( 1/ 0/ 2) |  0.50/0.25 ( 1/ 0/ 2)
  26  [ ]  dis    s24   0.3611  "Polis needs to support transla..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.70/0.10 ( 6/ 0/ 8)
  27  [ ]  dis    s5    0.3611  "Tooling for multiple moderator..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.50/0.10 ( 4/ 0/ 8)
  28  [ ]  dis    s10   0.3611  "Comments should follow a narra..."
                                     0.40/0.40 ( 1/ 1/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.30/0.30 ( 2/ 2/ 8)
  29  [ ]  dis    s19   0.3556  "Polis feels too abstract and a..."
                                     0.40/0.60 ( 1/ 2/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.77/0.23 ( 9/ 2/11)
  30  [ ]  dis    s9    0.3333  "Due to the 140 character limit..."
                                     0.20/0.80 ( 0/ 3/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.67/0.17 ( 7/ 1/10)
  31  [ ]  dis    s35   0.3333  "Set a slightly higher characte..."
                                     0.33/0.67 ( 0/ 1/ 1) |  0.33/0.33 ( 0/ 0/ 1) |  0.60/0.20 ( 2/ 0/ 3)
  32  [ ]  dis    s2    0.3333  "There's no way to differentiat..."
                                     0.25/0.50 ( 0/ 1/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.60/0.30 ( 5/ 2/ 8)
  33  [ ]  agree  s0    0.3333  "Polis is perfect just the way ..."
                                     0.25/0.75 ( 0/ 2/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.10/0.90 ( 0/ 8/ 8)
  34  [ ]  agree  s36   0.3125  "Give participants feedback abo..."
                                     0.67/0.33 ( 1/ 0/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.75/0.25 ( 2/ 0/ 2)
  35  [ ]  agree  s38   0.3000  "Fix log in"
                                     0.67/0.33 ( 1/ 0/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.80/0.20 ( 3/ 0/ 3)
  36  [ ]  dis    s27   0.2000  "I wish statements weren't limi..."
                                     0.25/0.50 ( 0/ 1/ 2) |  0.20/0.20 ( 0/ 0/ 3) |  0.75/0.12 ( 5/ 0/ 6)
  37  [ ]  agree  s20   0.1944  "It's hard to communicate techn..."
                                     0.20/0.80 ( 0/ 3/ 3) |  0.33/0.17 ( 1/ 0/ 4) |  0.73/0.27 ( 7/ 2/ 9)
  38  [ ]  dis    s8    0.1806  "Polis needs a way to showcase ..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.50/0.20 ( 4/ 1/ 8)
  39  [ ]  agree  s16   0.1667  "It sucks that there's no way t..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.33/0.17 ( 1/ 0/ 4) |  0.58/0.25 ( 6/ 2/10)
  40  [ ]  dis    s18   0.1667  "I am worried bad actors can sw..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.33/0.17 ( 1/ 0/ 4) |  0.70/0.20 ( 6/ 1/ 8)
  41  [ ]  dis    s4    0.1296  "There's no way to review previ..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.73/0.27 ( 7/ 2/ 9)
  42  [ ]  agree  s15   0.0648  "The inability to search for st..."
                                     0.40/0.40 ( 1/ 1/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.45/0.18 ( 4/ 1/ 9)
  
  --- Group 2 ---
   #  Sel  Dir    Stmt  Effect  Text
                                     G0 pa/pd (na/nd/ns) |  G1 pa/pd (na/nd/ns) |  G2 pa/pd (na/nd/ns)
   1  [*]  agree  s13   7.4380  "Polis statements can be too si..."
                                     0.20/0.80 ( 0/ 3/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.91/0.09 ( 9/ 0/ 9)
   2  [*]  agree  s9    4.0000  "Due to the 140 character limit..."
                                     0.20/0.80 ( 0/ 3/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.67/0.17 ( 7/ 1/10)
   3  [*]  agree  s27   3.9375  "I wish statements weren't limi..."
                                     0.25/0.50 ( 0/ 1/ 2) |  0.20/0.20 ( 0/ 0/ 3) |  0.75/0.12 ( 5/ 0/ 6)
   4  [ ]  agree  s2    2.8800  "There's no way to differentiat..."
                                     0.25/0.50 ( 0/ 1/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.60/0.30 ( 5/ 2/ 8)
   5  [*]  agree  s19   2.6627  "Polis feels too abstract and a..."
                                     0.40/0.60 ( 1/ 2/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.77/0.23 ( 9/ 2/11)
   6  [*]  agree  s17   2.4500  "I have no way to communicate t..."
                                     0.20/0.40 ( 0/ 1/ 3) |  0.29/0.29 ( 1/ 1/ 5) |  0.70/0.10 ( 6/ 0/ 8)
   7  [*]  agree  s20   2.3802  "It's hard to communicate techn..."
                                     0.20/0.80 ( 0/ 3/ 3) |  0.33/0.17 ( 1/ 0/ 4) |  0.73/0.27 ( 7/ 2/ 9)
   8  [ ]  agree  s21   1.9688  "I want to be able to share mor..."
                                     0.50/0.50 ( 1/ 1/ 2) |  0.20/0.60 ( 0/ 2/ 3) |  0.75/0.12 ( 5/ 0/ 6)
   9  [ ]  agree  s25   1.6200  "I want to be able to make a st..."
                                     0.40/0.60 ( 1/ 2/ 3) |  0.17/0.50 ( 0/ 2/ 4) |  0.60/0.30 ( 5/ 2/ 8)
  10  [*]  dis    s0    1.6200  "Polis is perfect just the way ..."
                                     0.25/0.75 ( 0/ 2/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.10/0.90 ( 0/ 8/ 8)
  11  [ ]  dis    s22   1.5868  "Polis relies on the participan..."
                                     0.60/0.40 ( 2/ 1/ 3) |  0.33/0.33 ( 1/ 1/ 4) |  0.18/0.73 ( 1/ 7/ 9)
  12  [ ]  agree  s35   1.4400  "Set a slightly higher characte..."
                                     0.33/0.67 ( 0/ 1/ 1) |  0.33/0.33 ( 0/ 0/ 1) |  0.60/0.20 ( 2/ 0/ 3)
  13  [ ]  agree  s3    1.4400  "Polis user-facing documentatio..."
                                     0.50/0.25 ( 1/ 0/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.60/0.10 ( 5/ 0/ 8)
  14  [ ]  agree  s4    1.1901  "There's no way to review previ..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.73/0.27 ( 7/ 2/ 9)
  15  [ ]  agree  s14   1.1852  "Polis should have a "remind me..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.17/0.50 ( 0/ 2/ 4) |  0.67/0.08 ( 7/ 0/10)
  16  [ ]  agree  s34   1.1111  "It asks for my email once I’ve..."
                                     0.33/0.67 ( 0/ 1/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.67/0.17 ( 3/ 0/ 4)
  17  [ ]  agree  s24   1.1025  "Polis needs to support transla..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.70/0.10 ( 6/ 0/ 8)
  18  [ ]  agree  s38   1.0667  "Fix log in"
                                     0.67/0.33 ( 1/ 0/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.80/0.20 ( 3/ 0/ 3)
  19  [ ]  agree  s6    1.0124  "It's unclear if Polis' algorit..."
                                     0.60/0.20 ( 2/ 0/ 3) |  0.29/0.43 ( 1/ 2/ 5) |  0.64/0.09 ( 6/ 0/ 9)
  20  [ ]  agree  s18   0.9800  "I am worried bad actors can sw..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.33/0.17 ( 1/ 0/ 4) |  0.70/0.20 ( 6/ 1/ 8)
  21  [*]  agree  s28   0.9481  "Questions that have been 'pass..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.75/0.25 ( 2/ 0/ 2) |  0.89/0.11 ( 7/ 0/ 7)
  22  [ ]  agree  s36   0.9375  "Give participants feedback abo..."
                                     0.67/0.33 ( 1/ 0/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.75/0.25 ( 2/ 0/ 2)
  23  [ ]  agree  s15   0.9298  "The inability to search for st..."
                                     0.40/0.40 ( 1/ 1/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.45/0.18 ( 4/ 1/ 9)
  24  [ ]  agree  s37   0.8889  "Admin option of setting a thre..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.67/0.33 ( 1/ 0/ 1)
  25  [ ]  agree  s26   0.6806  "I like how Polis relies on use..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.83/0.17 ( 4/ 0/ 4) |  0.78/0.11 ( 6/ 0/ 7)
  26  [ ]  agree  s7    0.6400  "The Polis website is not compl..."
                                     0.50/0.25 ( 1/ 0/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.40/0.20 ( 3/ 1/ 8)
  27  [ ]  agree  s16   0.6125  "It sucks that there's no way t..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.33/0.17 ( 1/ 0/ 4) |  0.58/0.25 ( 6/ 2/10)
  28  [ ]  agree  s8    0.5625  "Polis needs a way to showcase ..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.50/0.20 ( 4/ 1/ 8)
  29  [ ]  agree  s5    0.5625  "Tooling for multiple moderator..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.50/0.10 ( 4/ 0/ 8)
  30  [ ]  agree  s41   0.5000  "the interface is lack of space..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  31  [ ]  agree  s39   0.5000  "testing if this works when i s..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  32  [ ]  agree  s40   0.5000  "Testing out screen reader to s..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  33  [ ]  agree  s43   0.5000  "test"
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  34  [ ]  agree  s42   0.5000  "There is no clear visual hiera..."
                                     0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  35  [ ]  dis    s1    0.4800  "The prominent display of divis..."
                                     0.80/0.20 ( 3/ 0/ 3) |  0.17/0.50 ( 0/ 2/ 4) |  0.20/0.40 ( 1/ 3/ 8)
  36  [ ]  agree  s12   0.4800  "Polis is a very simple tool to..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.67/0.17 ( 3/ 0/ 4) |  0.60/0.20 ( 5/ 1/ 8)
  37  [ ]  agree  s30   0.4500  "Polis statements are atomic/bi..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.67/0.33 ( 1/ 0/ 1) |  0.60/0.20 ( 2/ 0/ 3)
  38  [ ]  agree  s10   0.4050  "Comments should follow a narra..."
                                     0.40/0.40 ( 1/ 1/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.30/0.30 ( 2/ 2/ 8)
  39  [ ]  agree  s31   0.3750  "Nuance in Polis is created by ..."
                                     0.75/0.25 ( 2/ 0/ 2) |  0.50/0.25 ( 1/ 0/ 2) |  0.50/0.25 ( 1/ 0/ 2)
  40  [ ]  agree  s23   0.3600  "There can be a bias against mi..."
                                     0.50/0.50 ( 1/ 1/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.30/0.20 ( 2/ 1/ 8)
  41  [ ]  agree  s32   0.3125  "There should be a QR code for ..."
                                     0.67/0.33 ( 1/ 0/ 1) |  0.75/0.25 ( 2/ 0/ 2) |  0.50/0.25 ( 1/ 0/ 2)
  42  [ ]  agree  s29   0.0694  "whether I engage through a tex..."
                                     0.33/0.67 ( 0/ 1/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.17/0.17 ( 0/ 0/ 4)
  
  === GROUP-AWARE CONSENSUS (AGREE) ===
   #  Stmt  GAC     Text
                            G0 pa (na/nd/ns) |  G1 pa (na/nd/ns) |  G2 pa (na/nd/ns)
   1  s26   0.6748  "I like how Polis relies on use..."
                            0.80 ( 3/ 0/ 3) |  0.83 ( 4/ 0/ 4) |  0.78 ( 6/ 0/ 7)
   2  s28   0.6300  "Questions that have been 'pass..."
                            0.75 ( 2/ 0/ 2) |  0.75 ( 2/ 0/ 2) |  0.89 ( 7/ 0/ 7)
   3  s12   0.5313  "Polis is a very simple tool to..."
                            0.75 ( 2/ 0/ 2) |  0.67 ( 3/ 0/ 4) |  0.60 ( 5/ 1/ 8)
   4  s30   0.4932  "Polis statements are atomic/bi..."
                            0.75 ( 2/ 0/ 2) |  0.67 ( 1/ 0/ 1) |  0.60 ( 2/ 0/ 3)
   5  s38   0.4743  "Fix log in"
                            0.67 ( 1/ 0/ 1) |  0.50 ( 1/ 0/ 2) |  0.80 ( 3/ 0/ 3)
   6  s36   0.4543  "Give participants feedback abo..."
                            0.67 ( 1/ 0/ 1) |  0.50 ( 1/ 0/ 2) |  0.75 ( 2/ 0/ 2)
   7  s32   0.4543  "There should be a QR code for ..."
                            0.67 ( 1/ 0/ 1) |  0.75 ( 2/ 0/ 2) |  0.50 ( 1/ 0/ 2)
   8  s18   0.4440  "I am worried bad actors can sw..."
                            0.75 ( 2/ 0/ 2) |  0.33 ( 1/ 0/ 4) |  0.70 ( 6/ 1/ 8)
   9  s31   0.4293  "Nuance in Polis is created by ..."
                            0.75 ( 2/ 0/ 2) |  0.50 ( 1/ 0/ 2) |  0.50 ( 1/ 0/ 2)
  10  s16   0.4269  "It sucks that there's no way t..."
                            0.80 ( 3/ 0/ 3) |  0.33 ( 1/ 0/ 4) |  0.58 ( 6/ 2/10)
  11  s24   0.3826  "Polis needs to support transla..."
                            0.80 ( 3/ 0/ 3) |  0.17 ( 0/ 0/ 4) |  0.70 ( 6/ 0/ 8)
  12  s4    0.3609  "There's no way to review previ..."
                            0.80 ( 3/ 0/ 3) |  0.17 ( 0/ 0/ 4) |  0.73 ( 7/ 2/ 9)
  13  s6    0.3566  "It's unclear if Polis' algorit..."
                            0.60 ( 2/ 0/ 3) |  0.29 ( 1/ 2/ 5) |  0.64 ( 6/ 0/ 9)
  14  s5    0.3420  "Tooling for multiple moderator..."
                            0.80 ( 3/ 0/ 3) |  0.17 ( 0/ 0/ 4) |  0.50 ( 4/ 0/ 8)
  15  s8    0.3288  "Polis needs a way to showcase ..."
                            0.80 ( 3/ 0/ 3) |  0.17 ( 0/ 0/ 4) |  0.50 ( 4/ 1/ 8)
  16  s14   0.3060  "Polis should have a "remind me..."
                            0.75 ( 2/ 0/ 2) |  0.17 ( 0/ 2/ 4) |  0.67 ( 7/ 0/10)
  17  s37   0.3029  "Admin option of setting a thre..."
                            0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0) |  0.67 ( 1/ 0/ 1)
  18  s34   0.2850  "It asks for my email once I’ve..."
                            0.33 ( 0/ 1/ 1) |  0.50 ( 1/ 0/ 2) |  0.67 ( 3/ 0/ 4)
  19  s3    0.2823  "Polis user-facing documentatio..."
                            0.50 ( 1/ 0/ 2) |  0.17 ( 0/ 1/ 4) |  0.60 ( 5/ 0/ 8)
  20  s39   0.2500  "testing if this works when i s..."
                            0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0)
  21  s40   0.2500  "Testing out screen reader to s..."
                            0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0)
  22  s41   0.2500  "the interface is lack of space..."
                            0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0)
  23  s42   0.2500  "There is no clear visual hiera..."
                            0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0)
  24  s43   0.2500  "test"
                            0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0)
  25  s17   0.2489  "I have no way to communicate t..."
                            0.20 ( 0/ 1/ 3) |  0.29 ( 1/ 1/ 5) |  0.70 ( 6/ 0/ 8)
  26  s7    0.2371  "The Polis website is not compl..."
                            0.50 ( 1/ 0/ 2) |  0.17 ( 0/ 1/ 4) |  0.40 ( 3/ 1/ 8)
  27  s21   0.2359  "I want to be able to share mor..."
                            0.50 ( 1/ 1/ 2) |  0.20 ( 0/ 2/ 3) |  0.75 ( 5/ 0/ 6)
  28  s27   0.2359  "I wish statements weren't limi..."
                            0.25 ( 0/ 1/ 2) |  0.20 ( 0/ 0/ 3) |  0.75 ( 5/ 0/ 6)
  29  s15   0.2314  "The inability to search for st..."
                            0.40 ( 1/ 1/ 3) |  0.17 ( 0/ 0/ 4) |  0.45 ( 4/ 1/ 9)
  30  s35   0.2280  "Set a slightly higher characte..."
                            0.33 ( 0/ 1/ 1) |  0.33 ( 0/ 0/ 1) |  0.60 ( 2/ 0/ 3)
  31  s19   0.2191  "Polis feels too abstract and a..."
                            0.40 ( 1/ 2/ 3) |  0.17 ( 0/ 1/ 4) |  0.77 ( 9/ 2/11)
  32  s23   0.1882  "There can be a bias against mi..."
                            0.50 ( 1/ 1/ 2) |  0.17 ( 0/ 1/ 4) |  0.30 ( 2/ 1/ 8)
  33  s1    0.1857  "The prominent display of divis..."
                            0.80 ( 3/ 0/ 3) |  0.17 ( 0/ 2/ 4) |  0.20 ( 1/ 3/ 8)
  34  s20   0.1805  "It's hard to communicate techn..."
                            0.20 ( 0/ 3/ 3) |  0.33 ( 1/ 0/ 4) |  0.73 ( 7/ 2/ 9)
  35  s2    0.1800  "There's no way to differentiat..."
                            0.25 ( 0/ 1/ 2) |  0.17 ( 0/ 1/ 4) |  0.60 ( 5/ 2/ 8)
  36  s29   0.1795  "whether I engage through a tex..."
                            0.33 ( 0/ 1/ 1) |  0.50 ( 1/ 0/ 2) |  0.17 ( 0/ 0/ 4)
  37  s10   0.1776  "Comments should follow a narra..."
                            0.40 ( 1/ 1/ 3) |  0.17 ( 0/ 1/ 4) |  0.30 ( 2/ 2/ 8)
  38  s25   0.1776  "I want to be able to make a st..."
                            0.40 ( 1/ 2/ 3) |  0.17 ( 0/ 2/ 4) |  0.60 ( 5/ 2/ 8)
  39  s22   0.1583  "Polis relies on the participan..."
                            0.60 ( 2/ 1/ 3) |  0.33 ( 1/ 1/ 4) |  0.18 ( 1/ 7/ 9)
  40  s13   0.1543  "Polis statements can be too si..."
                            0.20 ( 0/ 3/ 3) |  0.17 ( 0/ 1/ 4) |  0.91 ( 9/ 0/ 9)
  41  s9    0.1352  "Due to the 140 character limit..."
                            0.20 ( 0/ 3/ 3) |  0.17 ( 0/ 1/ 4) |  0.67 ( 7/ 1/10)
  42  s0    0.0411  "Polis is perfect just the way ..."
                            0.25 ( 0/ 2/ 2) |  0.17 ( 0/ 1/ 4) |  0.10 ( 0/ 8/ 8)
  
  === GROUP-AWARE CONSENSUS (DISAGREE) ===
   #  Stmt  GAC     Text
                            G0 pd (na/nd/ns) |  G1 pd (na/nd/ns) |  G2 pd (na/nd/ns)
   1  s0    0.5021  "Polis is perfect just the way ..."
                            0.75 ( 0/ 2/ 2) |  0.33 ( 0/ 1/ 4) |  0.90 ( 0/ 8/ 8)
   2  s22   0.2766  "Polis relies on the participan..."
                            0.40 ( 2/ 1/ 3) |  0.33 ( 1/ 1/ 4) |  0.73 ( 1/ 7/ 9)
   3  s25   0.2621  "I want to be able to make a st..."
                            0.60 ( 1/ 2/ 3) |  0.50 ( 0/ 2/ 4) |  0.30 ( 5/ 2/ 8)
   4  s39   0.2500  "testing if this works when i s..."
                            0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0)
   5  s40   0.2500  "Testing out screen reader to s..."
                            0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0)
   6  s41   0.2500  "the interface is lack of space..."
                            0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0)
   7  s42   0.2500  "There is no clear visual hiera..."
                            0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0)
   8  s43   0.2500  "test"
                            0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0)
   9  s10   0.2410  "Comments should follow a narra..."
                            0.40 ( 1/ 1/ 3) |  0.33 ( 0/ 1/ 4) |  0.30 ( 2/ 2/ 8)
  10  s2    0.2321  "There's no way to differentiat..."
                            0.50 ( 0/ 1/ 2) |  0.33 ( 0/ 1/ 4) |  0.30 ( 5/ 2/ 8)
  11  s9    0.2146  "Due to the 140 character limit..."
                            0.80 ( 0/ 3/ 3) |  0.33 ( 0/ 1/ 4) |  0.17 ( 7/ 1/10)
  12  s23   0.2134  "There can be a bias against mi..."
                            0.50 ( 1/ 1/ 2) |  0.33 ( 0/ 1/ 4) |  0.20 ( 2/ 1/ 8)
  13  s35   0.1992  "Set a slightly higher characte..."
                            0.67 ( 0/ 1/ 1) |  0.33 ( 0/ 0/ 1) |  0.20 ( 2/ 0/ 3)
  14  s29   0.1976  "whether I engage through a tex..."
                            0.67 ( 0/ 1/ 1) |  0.25 ( 1/ 0/ 2) |  0.17 ( 0/ 0/ 4)
  15  s37   0.1908  "Admin option of setting a thre..."
                            0.50 ( 0/ 0/ 0) |  0.50 ( 0/ 0/ 0) |  0.33 ( 1/ 0/ 1)
  16  s1    0.1747  "The prominent display of divis..."
                            0.20 ( 3/ 0/ 3) |  0.50 ( 0/ 2/ 4) |  0.40 ( 1/ 3/ 8)
  17  s19   0.1746  "Polis feels too abstract and a..."
                            0.60 ( 1/ 2/ 3) |  0.33 ( 0/ 1/ 4) |  0.23 ( 9/ 2/11)
  18  s20   0.1742  "It's hard to communicate techn..."
                            0.80 ( 0/ 3/ 3) |  0.17 ( 1/ 0/ 4) |  0.27 ( 7/ 2/ 9)
  19  s7    0.1609  "The Polis website is not compl..."
                            0.25 ( 1/ 0/ 2) |  0.33 ( 0/ 1/ 4) |  0.20 ( 3/ 1/ 8)
  20  s21   0.1554  "I want to be able to share mor..."
                            0.50 ( 1/ 1/ 2) |  0.60 ( 0/ 2/ 3) |  0.12 ( 5/ 0/ 6)
  21  s15   0.1490  "The inability to search for st..."
                            0.40 ( 1/ 1/ 3) |  0.17 ( 0/ 0/ 4) |  0.18 ( 4/ 1/ 9)
  22  s34   0.1456  "It asks for my email once I’ve..."
                            0.67 ( 0/ 1/ 1) |  0.25 ( 1/ 0/ 2) |  0.17 ( 3/ 0/ 4)
  23  s17   0.1251  "I have no way to communicate t..."
                            0.40 ( 0/ 1/ 3) |  0.29 ( 1/ 1/ 5) |  0.10 ( 6/ 0/ 8)
  24  s27   0.1233  "I wish statements weren't limi..."
                            0.50 ( 0/ 1/ 2) |  0.20 ( 0/ 0/ 3) |  0.12 ( 5/ 0/ 6)
  25  s13   0.1137  "Polis statements can be too si..."
                            0.80 ( 0/ 3/ 3) |  0.33 ( 0/ 1/ 4) |  0.09 ( 9/ 0/ 9)
  26  s3    0.1116  "Polis user-facing documentatio..."
                            0.25 ( 1/ 0/ 2) |  0.33 ( 0/ 1/ 4) |  0.10 ( 5/ 0/ 8)
  27  s31   0.0992  "Nuance in Polis is created by ..."
                            0.25 ( 2/ 0/ 2) |  0.25 ( 1/ 0/ 2) |  0.25 ( 1/ 0/ 2)
  28  s32   0.0954  "There should be a QR code for ..."
                            0.33 ( 1/ 0/ 1) |  0.25 ( 2/ 0/ 2) |  0.25 ( 1/ 0/ 2)
  29  s36   0.0954  "Give participants feedback abo..."
                            0.33 ( 1/ 0/ 1) |  0.25 ( 1/ 0/ 2) |  0.25 ( 2/ 0/ 2)
  30  s6    0.0932  "It's unclear if Polis' algorit..."
                            0.20 ( 2/ 0/ 3) |  0.43 ( 1/ 2/ 5) |  0.09 ( 6/ 0/ 9)
  31  s14   0.0898  "Polis should have a "remind me..."
                            0.25 ( 2/ 0/ 2) |  0.50 ( 0/ 2/ 4) |  0.08 ( 7/ 0/10)
  32  s30   0.0822  "Polis statements are atomic/bi..."
                            0.25 ( 2/ 0/ 2) |  0.33 ( 1/ 0/ 1) |  0.20 ( 2/ 0/ 3)
  33  s8    0.0822  "Polis needs a way to showcase ..."
                            0.20 ( 3/ 0/ 3) |  0.17 ( 0/ 0/ 4) |  0.20 ( 4/ 1/ 8)
  34  s38   0.0822  "Fix log in"
                            0.33 ( 1/ 0/ 1) |  0.25 ( 1/ 0/ 2) |  0.20 ( 3/ 0/ 3)
  35  s16   0.0774  "It sucks that there's no way t..."
                            0.20 ( 3/ 0/ 3) |  0.17 ( 1/ 0/ 4) |  0.25 ( 6/ 2/10)
  36  s18   0.0747  "I am worried bad actors can sw..."
                            0.25 ( 2/ 0/ 2) |  0.17 ( 1/ 0/ 4) |  0.20 ( 6/ 1/ 8)
  37  s4    0.0745  "There's no way to review previ..."
                            0.20 ( 3/ 0/ 3) |  0.17 ( 0/ 0/ 4) |  0.27 ( 7/ 2/ 9)
  38  s5    0.0652  "Tooling for multiple moderator..."
                            0.20 ( 3/ 0/ 3) |  0.17 ( 0/ 0/ 4) |  0.10 ( 4/ 0/ 8)
  39  s12   0.0652  "Polis is a very simple tool to..."
                            0.25 ( 2/ 0/ 2) |  0.17 ( 3/ 0/ 4) |  0.20 ( 5/ 1/ 8)
  40  s24   0.0550  "Polis needs to support transla..."
                            0.20 ( 3/ 0/ 3) |  0.17 ( 0/ 0/ 4) |  0.10 ( 6/ 0/ 8)
  41  s28   0.0364  "Questions that have been 'pass..."
                            0.25 ( 2/ 0/ 2) |  0.25 ( 2/ 0/ 2) |  0.11 ( 7/ 0/ 7)
  42  s26   0.0302  "I like how Polis relies on use..."
                            0.20 ( 3/ 0/ 3) |  0.17 ( 4/ 0/ 4) |  0.11 ( 6/ 0/ 7)
  
  === CONSENSUS STATEMENTS (AGREE) ===
   #  Sel  Stmt  Effect  pa    na/nd/ns  p_adj    Text
   1  [*]  s26   0.8889  0.89  15/ 0/16  0.0058  "I like how Polis relies on use..."
   2  [*]  s28   0.8750  0.88  13/ 1/14  0.0083  "Questions that have been 'pass..."
   3  [ ]  s32   0.7500  0.75   5/ 0/ 6  0.2359  "There should be a QR code for ..."
   4  [ ]  s30   0.7273  0.73   7/ 1/ 9  0.2359  "Polis statements are atomic/bi..."
   5  [ ]  s42   0.6667  0.67   1/ 0/ 1  0.2359  "There is no clear visual hiera..."
   6  [ ]  s36   0.6667  0.67   5/ 0/ 7  0.2359  "Give participants feedback abo..."
   7  [ ]  s43   0.6667  0.67   1/ 0/ 1  0.2359  "test"
   8  [ ]  s38   0.6667  0.67   5/ 1/ 7  0.2359  "Fix log in"
   9  [ ]  s39   0.6667  0.67   1/ 0/ 1  0.2359  "testing if this works when i s..."
  10  [ ]  s40   0.6667  0.67   1/ 0/ 1  0.2359  "Testing out screen reader to s..."
  11  [ ]  s41   0.6667  0.67   1/ 0/ 1  0.2359  "the interface is lack of space..."
  12  [ ]  s37   0.6667  0.67   1/ 0/ 1  0.2359  "Admin option of setting a thre..."
  13  [ ]  s18   0.6667  0.67  11/ 1/16  0.2359  "I am worried bad actors can sw..."
  14  [ ]  s12   0.6471  0.65  10/ 2/15  0.2359  "Polis is a very simple tool to..."
  15  [ ]  s4    0.6111  0.61  10/ 2/16  0.3154  "There's no way to review previ..."
  16  [ ]  s24   0.5882  0.59   9/ 0/15  0.4165  "Polis needs to support transla..."
  17  [ ]  s16   0.5714  0.57  11/ 2/19  0.4584  "It sucks that there's no way t..."
  18  [ ]  s21   0.5625  0.56   8/ 4/14  0.4690  "I want to be able to share mor..."
  19  [ ]  s34   0.5556  0.56   4/ 1/ 7  0.4690  "It asks for my email once I’ve..."
  20  [ ]  s14   0.5556  0.56   9/ 2/16  0.4690  "Polis should have a "remind me..."
  21  [ ]  s13   0.5556  0.56   9/ 4/16  0.4690  "Polis statements can be too si..."
  22  [ ]  s19   0.5500  0.55  10/ 5/18  0.4690  "Polis feels too abstract and a..."
  23  [ ]  s31   0.5455  0.55   5/ 0/ 9  0.4813  "Nuance in Polis is created by ..."
  24  [ ]  s6    0.5263  0.53   9/ 2/17  0.5577  "It's unclear if Polis' algorit..."
  25  [ ]  s20   0.5000  0.50   8/ 5/16  0.6529  "It's hard to communicate techn..."
  26  [ ]  s27   0.5000  0.50   6/ 1/12  0.6529  "I wish statements weren't limi..."
  27  [ ]  s5    0.4706  0.47   7/ 0/15  0.7500  "Tooling for multiple moderator..."
  28  [ ]  s8    0.4706  0.47   7/ 1/15  0.7500  "Polis needs a way to showcase ..."
  29  [ ]  s9    0.4500  0.45   8/ 5/18  0.8072  "Due to the 140 character limit..."
  30  [ ]  s17   0.4444  0.44   7/ 2/16  0.8072  "I have no way to communicate t..."
  31  [ ]  s25   0.4444  0.44   7/ 6/16  0.8072  "I want to be able to make a st..."
  32  [ ]  s3    0.4118  0.41   6/ 2/15  0.8800  "Polis user-facing documentatio..."
  33  [ ]  s35   0.3750  0.38   2/ 1/ 6  0.8495  "Set a slightly higher characte..."
  34  [ ]  s2    0.3750  0.38   5/ 4/14  0.9369  "There's no way to differentiat..."
  35  [ ]  s29   0.3636  0.36   3/ 1/ 9  0.9097  "whether I engage through a tex..."
  36  [ ]  s15   0.3333  0.33   5/ 2/16  0.9996  "The inability to search for st..."
  37  [ ]  s7    0.3125  0.31   4/ 2/14  0.9996  "The Polis website is not compl..."
  38  [ ]  s1    0.2941  0.29   4/ 5/15  0.9996  "The prominent display of divis..."
  39  [ ]  s22   0.2778  0.28   4/ 9/16  0.9996  "Polis relies on the participan..."
  40  [ ]  s23   0.2500  0.25   3/ 3/14  0.9996  "There can be a bias against mi..."
  41  [ ]  s10   0.2353  0.24   3/ 4/15  0.9996  "Comments should follow a narra..."
  42  [ ]  s0    0.0625  0.06   0/11/14  0.9996  "Polis is perfect just the way ..."
  
  === CONSENSUS STATEMENTS (DISAGREE) ===
   #  Sel  Stmt  Effect  pd    na/nd/ns  p_adj    Text
   1  [ ]  s0    0.7500  0.75   0/11/14  0.4229  "Polis is perfect just the way ..."
   2  [ ]  s22   0.5556  0.56   4/ 9/16  0.9999  "Polis relies on the participan..."
   3  [ ]  s25   0.3889  0.39   7/ 6/16  0.9999  "I want to be able to make a st..."
   4  [ ]  s1    0.3529  0.35   4/ 5/15  0.9999  "The prominent display of divis..."
   5  [ ]  s41   0.3333  0.33   1/ 0/ 1  0.9999  "the interface is lack of space..."
   6  [ ]  s40   0.3333  0.33   1/ 0/ 1  0.9999  "Testing out screen reader to s..."
   7  [ ]  s39   0.3333  0.33   1/ 0/ 1  0.9999  "testing if this works when i s..."
   8  [ ]  s37   0.3333  0.33   1/ 0/ 1  0.9999  "Admin option of setting a thre..."
   9  [ ]  s42   0.3333  0.33   1/ 0/ 1  0.9999  "There is no clear visual hiera..."
  10  [ ]  s20   0.3333  0.33   8/ 5/16  0.9999  "It's hard to communicate techn..."
  11  [ ]  s43   0.3333  0.33   1/ 0/ 1  0.9999  "test"
  12  [ ]  s21   0.3125  0.31   8/ 4/14  0.9999  "I want to be able to share mor..."
  13  [ ]  s2    0.3125  0.31   5/ 4/14  0.9999  "There's no way to differentiat..."
  14  [ ]  s19   0.3000  0.30  10/ 5/18  0.9999  "Polis feels too abstract and a..."
  15  [ ]  s9    0.3000  0.30   8/ 5/18  0.9999  "Due to the 140 character limit..."
  16  [ ]  s10   0.2941  0.29   3/ 4/15  0.9999  "Comments should follow a narra..."
  17  [ ]  s13   0.2778  0.28   9/ 4/16  0.9999  "Polis statements can be too si..."
  18  [ ]  s35   0.2500  0.25   2/ 1/ 6  0.9999  "Set a slightly higher characte..."
  19  [ ]  s23   0.2500  0.25   3/ 3/14  0.9999  "There can be a bias against mi..."
  20  [ ]  s38   0.2222  0.22   5/ 1/ 7  0.9999  "Fix log in"
  21  [ ]  s34   0.2222  0.22   4/ 1/ 7  0.9999  "It asks for my email once I’ve..."
  22  [ ]  s7    0.1875  0.19   4/ 2/14  0.9999  "The Polis website is not compl..."
  23  [ ]  s30   0.1818  0.18   7/ 1/ 9  0.9999  "Polis statements are atomic/bi..."
  24  [ ]  s29   0.1818  0.18   3/ 1/ 9  0.9999  "whether I engage through a tex..."
  25  [ ]  s3    0.1765  0.18   6/ 2/15  0.9999  "Polis user-facing documentatio..."
  26  [ ]  s12   0.1765  0.18  10/ 2/15  0.9999  "Polis is a very simple tool to..."
  27  [ ]  s17   0.1667  0.17   7/ 2/16  0.9999  "I have no way to communicate t..."
  28  [ ]  s4    0.1667  0.17  10/ 2/16  0.9999  "There's no way to review previ..."
  29  [ ]  s15   0.1667  0.17   5/ 2/16  0.9999  "The inability to search for st..."
  30  [ ]  s14   0.1667  0.17   9/ 2/16  0.9999  "Polis should have a "remind me..."
  31  [ ]  s6    0.1579  0.16   9/ 2/17  0.9999  "It's unclear if Polis' algorit..."
  32  [ ]  s16   0.1429  0.14  11/ 2/19  0.9999  "It sucks that there's no way t..."
  33  [ ]  s27   0.1429  0.14   6/ 1/12  0.9999  "I wish statements weren't limi..."
  34  [ ]  s28   0.1250  0.12  13/ 1/14  0.9999  "Questions that have been 'pass..."
  35  [ ]  s32   0.1250  0.12   5/ 0/ 6  0.9999  "There should be a QR code for ..."
  36  [ ]  s8    0.1176  0.12   7/ 1/15  0.9999  "Polis needs a way to showcase ..."
  37  [ ]  s18   0.1111  0.11  11/ 1/16  0.9999  "I am worried bad actors can sw..."
  38  [ ]  s36   0.1111  0.11   5/ 0/ 7  0.9999  "Give participants feedback abo..."
  39  [ ]  s31   0.0909  0.09   5/ 0/ 9  0.9999  "Nuance in Polis is created by ..."
  40  [ ]  s24   0.0588  0.06   9/ 0/15  0.9999  "Polis needs to support transla..."
  41  [ ]  s5    0.0588  0.06   7/ 0/15  0.9999  "Tooling for multiple moderator..."
  42  [ ]  s26   0.0556  0.06  15/ 0/16  0.9999  "I like how Polis relies on use..."
  
  === DIVISIVE STATEMENTS ===
   #  Stmt  Div     Text
                            G0 pa/pd (na/nd/ns) |  G1 pa/pd (na/nd/ns) |  G2 pa/pd (na/nd/ns)
   1  s13   0.7424  "Polis statements can be too si..."
                            0.20/0.80 ( 0/ 3/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.91/0.09 ( 9/ 0/ 9)
   2  s1    0.6333  "The prominent display of divis..."
                            0.80/0.20 ( 3/ 0/ 3) |  0.17/0.50 ( 0/ 2/ 4) |  0.20/0.40 ( 1/ 3/ 8)
   3  s4    0.6333  "There's no way to review previ..."
                            0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.73/0.27 ( 7/ 2/ 9)
   4  s5    0.6333  "Tooling for multiple moderator..."
                            0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.50/0.10 ( 4/ 0/ 8)
   5  s8    0.6333  "Polis needs a way to showcase ..."
                            0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.50/0.20 ( 4/ 1/ 8)
   6  s24   0.6333  "Polis needs to support transla..."
                            0.80/0.20 ( 3/ 0/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.70/0.10 ( 6/ 0/ 8)
   7  s19   0.6026  "Polis feels too abstract and a..."
                            0.40/0.60 ( 1/ 2/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.77/0.23 ( 9/ 2/11)
   8  s14   0.5833  "Polis should have a "remind me..."
                            0.75/0.25 ( 2/ 0/ 2) |  0.17/0.50 ( 0/ 2/ 4) |  0.67/0.08 ( 7/ 0/10)
   9  s21   0.5500  "I want to be able to share mor..."
                            0.50/0.50 ( 1/ 1/ 2) |  0.20/0.60 ( 0/ 2/ 3) |  0.75/0.12 ( 5/ 0/ 6)
  10  s27   0.5500  "I wish statements weren't limi..."
                            0.25/0.50 ( 0/ 1/ 2) |  0.20/0.20 ( 0/ 0/ 3) |  0.75/0.12 ( 5/ 0/ 6)
  11  s20   0.5273  "It's hard to communicate techn..."
                            0.20/0.80 ( 0/ 3/ 3) |  0.33/0.17 ( 1/ 0/ 4) |  0.73/0.27 ( 7/ 2/ 9)
  12  s9    0.5000  "Due to the 140 character limit..."
                            0.20/0.80 ( 0/ 3/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.67/0.17 ( 7/ 1/10)
  13  s17   0.5000  "I have no way to communicate t..."
                            0.20/0.40 ( 0/ 1/ 3) |  0.29/0.29 ( 1/ 1/ 5) |  0.70/0.10 ( 6/ 0/ 8)
  14  s16   0.4667  "It sucks that there's no way t..."
                            0.80/0.20 ( 3/ 0/ 3) |  0.33/0.17 ( 1/ 0/ 4) |  0.58/0.25 ( 6/ 2/10)
  15  s2    0.4333  "There's no way to differentiat..."
                            0.25/0.50 ( 0/ 1/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.60/0.30 ( 5/ 2/ 8)
  16  s3    0.4333  "Polis user-facing documentatio..."
                            0.50/0.25 ( 1/ 0/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.60/0.10 ( 5/ 0/ 8)
  17  s25   0.4333  "I want to be able to make a st..."
                            0.40/0.60 ( 1/ 2/ 3) |  0.17/0.50 ( 0/ 2/ 4) |  0.60/0.30 ( 5/ 2/ 8)
  18  s22   0.4182  "Polis relies on the participan..."
                            0.60/0.40 ( 2/ 1/ 3) |  0.33/0.33 ( 1/ 1/ 4) |  0.18/0.73 ( 1/ 7/ 9)
  19  s18   0.4167  "I am worried bad actors can sw..."
                            0.75/0.25 ( 2/ 0/ 2) |  0.33/0.17 ( 1/ 0/ 4) |  0.70/0.20 ( 6/ 1/ 8)
  20  s6    0.3506  "It's unclear if Polis' algorit..."
                            0.60/0.20 ( 2/ 0/ 3) |  0.29/0.43 ( 1/ 2/ 5) |  0.64/0.09 ( 6/ 0/ 9)
  21  s7    0.3333  "The Polis website is not compl..."
                            0.50/0.25 ( 1/ 0/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.40/0.20 ( 3/ 1/ 8)
  22  s23   0.3333  "There can be a bias against mi..."
                            0.50/0.50 ( 1/ 1/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.30/0.20 ( 2/ 1/ 8)
  23  s29   0.3333  "whether I engage through a tex..."
                            0.33/0.67 ( 0/ 1/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.17/0.17 ( 0/ 0/ 4)
  24  s34   0.3333  "It asks for my email once I’ve..."
                            0.33/0.67 ( 0/ 1/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.67/0.17 ( 3/ 0/ 4)
  25  s38   0.3000  "Fix log in"
                            0.67/0.33 ( 1/ 0/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.80/0.20 ( 3/ 0/ 3)
  26  s15   0.2879  "The inability to search for st..."
                            0.40/0.40 ( 1/ 1/ 3) |  0.17/0.17 ( 0/ 0/ 4) |  0.45/0.18 ( 4/ 1/ 9)
  27  s35   0.2667  "Set a slightly higher characte..."
                            0.33/0.67 ( 0/ 1/ 1) |  0.33/0.33 ( 0/ 0/ 1) |  0.60/0.20 ( 2/ 0/ 3)
  28  s31   0.2500  "Nuance in Polis is created by ..."
                            0.75/0.25 ( 2/ 0/ 2) |  0.50/0.25 ( 1/ 0/ 2) |  0.50/0.25 ( 1/ 0/ 2)
  29  s32   0.2500  "There should be a QR code for ..."
                            0.67/0.33 ( 1/ 0/ 1) |  0.75/0.25 ( 2/ 0/ 2) |  0.50/0.25 ( 1/ 0/ 2)
  30  s36   0.2500  "Give participants feedback abo..."
                            0.67/0.33 ( 1/ 0/ 1) |  0.50/0.25 ( 1/ 0/ 2) |  0.75/0.25 ( 2/ 0/ 2)
  31  s10   0.2333  "Comments should follow a narra..."
                            0.40/0.40 ( 1/ 1/ 3) |  0.17/0.33 ( 0/ 1/ 4) |  0.30/0.30 ( 2/ 2/ 8)
  32  s37   0.1667  "Admin option of setting a thre..."
                            0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.67/0.33 ( 1/ 0/ 1)
  33  s12   0.1500  "Polis is a very simple tool to..."
                            0.75/0.25 ( 2/ 0/ 2) |  0.67/0.17 ( 3/ 0/ 4) |  0.60/0.20 ( 5/ 1/ 8)
  34  s30   0.1500  "Polis statements are atomic/bi..."
                            0.75/0.25 ( 2/ 0/ 2) |  0.67/0.33 ( 1/ 0/ 1) |  0.60/0.20 ( 2/ 0/ 3)
  35  s0    0.1500  "Polis is perfect just the way ..."
                            0.25/0.75 ( 0/ 2/ 2) |  0.17/0.33 ( 0/ 1/ 4) |  0.10/0.90 ( 0/ 8/ 8)
  36  s28   0.1389  "Questions that have been 'pass..."
                            0.75/0.25 ( 2/ 0/ 2) |  0.75/0.25 ( 2/ 0/ 2) |  0.89/0.11 ( 7/ 0/ 7)
  37  s26   0.0556  "I like how Polis relies on use..."
                            0.80/0.20 ( 3/ 0/ 3) |  0.83/0.17 ( 4/ 0/ 4) |  0.78/0.11 ( 6/ 0/ 7)
  38  s39   0.0000  "testing if this works when i s..."
                            0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  39  s40   0.0000  "Testing out screen reader to s..."
                            0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  40  s41   0.0000  "the interface is lack of space..."
                            0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  41  s42   0.0000  "There is no clear visual hiera..."
                            0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  42  s43   0.0000  "test"
                            0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0) |  0.50/0.50 ( 0/ 0/ 0)
  
  === SELECTION COMPARISON ===
  
  --- Repness ---
  Group 0:
    Polis (pick_max=5): s1(a) s13(d) s9(d) s20(d) s29(d)
    Agora (BH fdr=0.10): s13(d) s1(a) s9(d) s20(d)
  Group 1:
    Polis (pick_max=5): s26(a)
    Agora (BH fdr=0.10): (none)
  Group 2:
    Polis (pick_max=5): s13(a) s27(a) s19(a) s9(a) s0(d)
    Agora (BH fdr=0.10): s13(a) s9(a) s27(a) s19(a) s17(a) s20(a) s0(d) s28(a)
  
  --- Consensus (agree) ---
    Polis (pick_max=5): s26 s28 s32 s30 s18
    Agora (BH fdr=0.10): s26 s28
  
  --- Consensus (disagree) ---
    Polis (pick_max=5): s0
    Agora (BH fdr=0.10): (none)
