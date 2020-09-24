/*select Track.Name as "Song Name", MediaType.Name as "Media Type", Genre.Name as "Music Genre" from Track
inner join MediaType on Track.MediaTypeId = MediaType.MediaTypeId
inner join Genre on Track.GenreId = Genre.GenreId
where Genre.Name = "SoundTrack" and MediaType.Name = "Protected AAC audio file";*/ 

/*select Playlist.Name as Playlist, Track.Name as "Song Name", Album.Title as "Album Name", Artist.Name as Artist from Playlist
inner join PlaylistTrack on Playlist.PlaylistId = PlaylistTrack.PlaylistId
inner join Track on PlaylistTrack.TrackId = Track.TrackId
inner join Album on Track.AlbumId = Album.AlbumId
inner join Artist on Album.ArtistId = Artist.ArtistId;*/

/*select count(*) from Customer inner join Employee on Customer.SupportRepId = Employee.EmployeeId where Employee.FirstName = "Jane" and Employee.LastName = "Peacock";*/ 

/*select MediaType.Name, count(*) from Track
inner join MediaType on Track.MediaTypeId = MediaType.MediaTypeId
group by MediaType.Name
order by count(*) desc
limit 1;*/

/*select MIN(BirthDate) from Employee;*/

/*select MAX(HireDate) from Employee;*/

/*select ROUND(AVG(Total),2) from Invoice; result rounded to 2 dp*/

/*select City, count(*) from Customer
group by City
order by City asc;*/

/*select Name as "Track", ROUND(SUM(InvoiceLine.UnitPrice*InvoiceLine.Quantity),2) as "Total" from Track
inner join InvoiceLine on Track.TrackId = InvoiceLine.TrackId
where Name  = "The Woman King";*/

/*select Artist.Name, count(*) from Track
inner join Album on Track.AlbumId = Album.AlbumId
inner join Artist on Album.ArtistId = Artist.ArtistId
group by Artist.Name
order by count(*) desc
limit 5;*/