<?php

$fileArray = file('input');

$correctCount = 0;

foreach ($fileArray as $line)
{
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
		if (array_key_exists($count, $score))
		{
			$score[$count] .= $letter;
		}
		else
		{
			$score[$count] = $letter;
		}
	}

	$word = '';

	foreach ($lettersArray as $letters => $count)
	{
		$length = strlen($word);

		if ($length < 5)
		{
			$toSort = str_split($letters);
			sort($toSort);
			$sorted = implode('', $toSort);


		}
		else
		{
			break;
		}
	}

	print_r($score);
}

?>