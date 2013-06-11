/*jslint white: true */
/*global mw, $ */
if ( mw.config.get( 'wgPageName' ).indexOf( 'Wikipédia:Projetos/' ) !== -1 ) {
	//[[MediaWiki:Gadget-newParticipant wikiProjects.js/Core.js]]
	mw.loader.load( 'ext.gadget.newParticipantWikiProjectsCore' );
}