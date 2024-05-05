CREATE PROCEDURE GetAllVendorInfo
	@vendor_id INT
	@vendor_name VARCHAR
AS 
BEGIN
	SELECT * FROM public.vendor_vendor
ORDER BY id ASC 
END;