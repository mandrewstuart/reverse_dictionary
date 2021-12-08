the model is from https://tfhub.dev/google/universal-sentence-encoder-multilingual/3

put it in model-directory or put a different one together yourself!

It creates a sqlite3 database in a file called file.db so that you don't have to spend the time to recreate the vectors every time.

Also, the dictionary can be found at:
https://github.com/sujithps/Dictionary/blob/master/Oxford%20English%20Dictionary.txt

Or you can supply your own but you'll likely have to modify the parser.

Example:
Describe the word you're thinking of and press enter:
a thing that you sit on
['Seat', "—n. 1 thing made or used for sitting on. 2 a buttocks. B part of a garment covering them. 3 part of a chair etc. On which the buttocks rest. 4 place for one person in a theatre etc. 5 position as an mp, committee member, etc., or the right to occupy it. 6 supporting or guiding part of a machine. 7 location (seat of learning). 8 country mansion. 9 manner of sitting on a horse etc. —v. 1 cause to sit. 2 provide sitting accommodation for (bus seats 50). 3 (as seated adj.) Sitting. 4 put or fit in position. be seated sit down. By the seat of one's pants colloq. By instinct rather than knowledge. Take a seat sit down. "]
['Footstool', 'n. Stool for resting the feet on when sitting.']
['Sitting-room', 'n. Room for relaxed sitting in.']
['Sitting', '—n. 1 continuous period spent engaged in an activity (finished the book in one sitting). 2 time during which an assembly is engaged in business. 3 session in which a meal is served. —adj. 1 having sat down. 2 (of an animal or bird) still. 3 (of an mp etc.) Current.']
['Bucket seat', 'n. Seat with a rounded back for one person, esp. In a car.']
['Settee', 'n. = *sofa. ']
['Leg-room', 'n. Space for the legs of a seated person.']
['Sit-in', 'n. Protest involving sitting in.']
['Sit-down', '—attrib. Adj. 1 (of a meal) eaten sitting at a table. 2 (of a protest etc.) With demonstrators occupying their workplace or sitting down on the ground in a public place. —n. 1 spell of sitting. 2 sit-down protest etc.']
['Hip-bath', 'n. Portable bath in which one sits immersed to the hips.']
['Drive-in', "—attrib. Adj. (of a bank, cinema, etc.) Used while sitting in one's car. —n. Such a bank, cinema, etc."]
['Tier', 'n. Row, rank, or unit of a structure, as one of several placed one above another (tiers of seats). tiered adj. ']
['Loll', 'v. 1 stand, sit, or recline in a lazy attitude. 2 hang loosely. ']
['Sedentary', 'adj. 1 sitting. 2 (of work etc.) Done while sitting. 3 (of a person) disinclined to exercise. ']
['Swivel chair', 'n. Chair with a revolving seat.']

to create the cache, use database_version.prepare()
and once it's done, then you can run main.main()