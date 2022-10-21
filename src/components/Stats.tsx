import React from 'react';

function Stats() {
	return (
		<div className="border border-stone-50 w-1/4 h-5/6 flex-initial flex flex-col text-white text-center">
            <p>STATS</p>

            <p className='mt-5'>Last weight</p>
            <div id='current-weight' className='mx-10 flex flex-row justify-between'>
                <div>XX kg</div>
                <div>ab/cd/ef</div> {/* Alleen zichtbaar bij >small screen */}
            </div>
            <p>Highest weight</p>
            <div id='highest-weight' className='mx-10 flex flex-row justify-between'>
                <div>XX kg</div>
                <div>ab/cd/ef</div> {/* Alleen zichtbaar bij >small screen */}
            </div>
            <p>Lowest weight</p>
            <div id='lowest-weight' className='mx-10 flex flex-row justify-between'>
                <div>XX kg</div>
                <div>ab/cd/ef</div> {/* Alleen zichtbaar bij >small screen */}
            </div>

            <p className='mt-5'>Last bodyfat %</p>
            <div id='current-bf' className='mx-10 flex flex-row justify-between'>
                <div>XX %</div>
                <div>ab/cd/ef</div> {/* Alleen zichtbaar bij >small screen */}
            </div>
            <p>Highest bodyfat %</p>
            <div id='highest-bf' className='mx-10 flex flex-row justify-between'>
                <div>XX %</div>
                <div>ab/cd/ef</div> {/* Alleen zichtbaar bij >small screen */}
            </div>
            <p>Lowest bodyfat %</p>
            <div id='lowest-bf' className='mx-10 flex flex-row justify-between'>
                <div>XX %</div>
                <div>ab/cd/ef</div> {/* Alleen zichtbaar bij >small screen */}
            </div>
		</div>
	);
}

export default Stats;
