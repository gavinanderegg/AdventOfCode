<?php

$fileArray = file('input');

$correctCount = 0;
$wordLength = 5;

foreach ($fileArray as $line)
{
	$line = trim($line);

	print "\nLooking at: $line";

	$matches = array();
	preg_match('/([a-z\-]{1,})\d+\[([a-z]{5})\]/', $line, $matches);

	$letters = str_replace('-', '', $matches[1]);
	$lettersArray = str_split($letters);
	$lettersArray = array_count_values($lettersArray);
	arsort($lettersArray);

	$top = $matches[2];

	$score = array();

	foreach ($lettersArray as $letter => $count)
	{
		if (!array_key_exists($count, $score))
		{
			$score[$count] = '';
		}

		$score[$count] .= $letter;
	}

	print "Scored letters:\n";

	print_r($score);

	$word = '';

	foreach ($score as $count => $letters)
	{
		$length = strlen($word);

		if ($length < 5)
		{
			$sorted = str_split($letters);
			sort($sorted);

			if (count($sorted) < ($wordLength - $length))
			{
				foreach ($sorted as $letter)
				{
					$word .= $letter;
				}
			}
			else
			{
				$i = 0;

				while (strlen($word) < $wordLength)
				{
					$word .= $sorted[$i];
					$i++;
				}
			}
		}
		else
		{
			break;
		}
	}

	print "I think the word is:   $word\n";
	print "The top word is:       $top\n";

	if ($word == $top)
	{
		$correctCount += 1;

		print "Looks correct!\n";
	}
	else
	{
		print "Nope!\n";
	}
}

print "\n" . $correctCount . "\n"

?>