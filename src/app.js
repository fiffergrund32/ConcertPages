//initialize instantsearch
const search = instantsearch({
  indexName: 'casey_rainmaker',
  searchClient: algoliasearch('4P0IPJPNC7', 'cdd3dbbb9f591f405f2b8fdcfce3ea4a'),
});

search.addWidgets([
	instantsearch.widgets.searchBox({
		container: '#searchbox',
		placeholder: 'Search for an artist, venue, or date',
	}),
	instantsearch.widgets.clearRefinements({
		container: '#clear-refinements',
	}),
	instantsearch.widgets.refinementList({
		container: '#venue-list',
		attribute: 'location',
		limit: '20',
		showMore: 'true',
		showMoreLimit: '30',
	}),
	instantsearch.widgets.hitsPerPage({
		container: '#hits-per-page',
		items: [
		{ label: '10 hits per page', value: 10, default: true },
		{ label: '15 hits per page', value: 15 },
		{ label: '20 hits per page', value: 20 },
		],
	}),
	instantsearch.widgets.hits({
    container: '#hits',
    templates: {
      item: `
        <div>
          <div class="hit-name">
            <h2>
			{{#helpers.highlight}}{ "attribute": "name" }{{/helpers.highlight}}
			</h2>
          </div>
		  <div class="hit-location">
			{{#helpers.highlight}}{ "attribute": "location" }{{/helpers.highlight}}
		  </div>
          <div class="hit-date">
		    <h3>
			{{#helpers.highlight}}{ "attribute": "date" }{{/helpers.highlight}}
			</h3>
		  </div>
        </div>
      `,
    },
	}),
	instantsearch.widgets.pagination({
		container: '#pagination',
	}),
]);


search.start();
