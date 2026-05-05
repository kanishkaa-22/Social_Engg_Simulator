# Test Scenarios - Social Engineering Simulator

Test the application with these scenarios to verify login event logging works correctly.

## Scenario 1: Successful Login
**Objective**: Verify successful login is logged

**Steps**:
1. Go to http://127.0.0.1:5000/login
2. Enter Username: `po`
3. Enter Password: `po`
4. Click Login button

**Expected Result**:
- ✓ Redirected to dashboard: "Welcome, po!"
- ✓ Entry appears in login_events.txt with Status: SUCCESS
- ✓ Terminal shows: "Status    : SUCCESS"

**Sample Log Entry**:
```
====== LOGIN EVENT ======
Time      : 2026-04-30 14:30:15.456789
Username  : po
Password  : po
Status    : SUCCESS
=========================
```

---

## Scenario 2: Failed Login - Wrong Password
**Objective**: Verify failed login attempt is logged

**Steps**:
1. Go to http://127.0.0.1:5000/login
2. Enter Username: `po`
3. Enter Password: `wrongpassword`
4. Click Login button

**Expected Result**:
- ✗ Stays on login page
- ✗ Error message shows: "Invalid credentials. Please try again."
- ✓ Entry appears in login_events.txt with Status: FAILED
- ✓ Terminal shows: "Status    : FAILED"

**Sample Log Entry**:
```
====== LOGIN EVENT ======
Time      : 2026-04-30 14:31:45.789123
Username  : po
Password  : wrongpassword
Status    : FAILED
=========================
```

---

## Scenario 3: Failed Login - User Not Found
**Objective**: Verify non-existent user login is logged

**Steps**:
1. Go to http://127.0.0.1:5000/login
2. Enter Username: `nonexistentuser`
3. Enter Password: `anypassword`
4. Click Login button

**Expected Result**:
- ✗ Stays on login page
- ✗ Error message shows: "Invalid credentials. Please try again."
- ✓ Entry appears in login_events.txt with Status: FAILED
- ✓ Terminal shows: "Status    : FAILED"

**Sample Log Entry**:
```
====== LOGIN EVENT ======
Time      : 2026-04-30 14:32:20.345678
Username  : nonexistentuser
Password  : anypassword
Status    : FAILED
=========================
```

---

## Scenario 4: Multiple Login Attempts
**Objective**: Verify multiple attempts are all logged

**Steps**:
1. Attempt login 3 times with different credentials:
   - Attempt 1: `po` / `wrong` (FAILED)
   - Attempt 2: `asd` / `asd` (SUCCESS)
   - Attempt 3: `asdf` / `asdf` (SUCCESS)

**Expected Result**:
- ✓ All 3 events logged in login_events.txt
- ✓ File contains 3 separate login event entries
- ✓ Timestamps are different (or same second, but in sequence)
- ✓ Statuses correctly show SUCCESS/FAILED

**What login_events.txt should look like**:
```
====== LOGIN EVENT ======
Time      : 2026-04-30 14:33:01.111111
Username  : po
Password  : wrong
Status    : FAILED
=========================

====== LOGIN EVENT ======
Time      : 2026-04-30 14:33:15.222222
Username  : asd
Password  : asd
Status    : SUCCESS
=========================

====== LOGIN EVENT ======
Time      : 2026-04-30 14:33:25.333333
Username  : asdf
Password  : asdf
Status    : SUCCESS
=========================
```

---

## Scenario 5: Special Characters in Password
**Objective**: Verify special characters are logged correctly

**Steps**:
1. Go to http://127.0.0.1:5000/login
2. Enter Username: `qwdf`
3. Enter Password: `qwef` (note: 'qwef' not 'qwdf')
4. Click Login button

**Expected Result**:
- ✗ Stays on login page (credentials don't match exactly)
- ✗ Error message shows: "Invalid credentials. Please try again."
- ✓ Entry appears in login_events.txt with Status: FAILED
- ✓ Password 'qwef' is logged exactly as entered

---

## Scenario 6: Case Sensitivity
**Objective**: Verify credentials are case-sensitive

**Steps**:
1. Go to http://127.0.0.1:5000/login
2. Enter Username: `PO` (uppercase)
3. Enter Password: `po` (lowercase)
4. Click Login button

**Expected Result**:
- ✗ Stays on login page
- ✗ Error message shows: "Invalid credentials. Please try again."
- ✓ Entry appears in login_events.txt with Status: FAILED
- ✓ Username 'PO' is logged exactly as entered

---

## Scenario 7: Empty Fields
**Objective**: Verify form requires both fields

**Steps**:
1. Go to http://127.0.0.1:5000/login
2. Leave username and password empty
3. Try to click Login button

**Expected Result**:
- Browser shows validation error: "Please fill out this field."
- Event is NOT logged (validation happens client-side)
- Form prevents submission

---

## Scenario 8: Verify Log File Growth
**Objective**: Confirm login_events.txt is properly appended

**Steps**:
1. Open login_events.txt and note the number of entries
2. Perform 2-3 new login attempts
3. Reopen login_events.txt

**Expected Result**:
- ✓ File size has increased
- ✓ New entries are appended (not replacing old ones)
- ✓ All previous entries still present
- ✓ New entries appear at the end

---

## Scenario 9: Timestamp Accuracy
**Objective**: Verify timestamps are accurate

**Steps**:
1. Check current system time
2. Attempt login
3. View login_events.txt

**Expected Result**:
- ✓ Timestamp in log matches actual time
- ✓ Timestamp format: YYYY-MM-DD HH:MM:SS.ffffff
- ✓ Includes microseconds for precision

---

## Scenario 10: Terminal Output
**Objective**: Verify logs appear in terminal/console

**Steps**:
1. Start app from terminal/PowerShell where you can see output
2. Perform a login attempt
3. Observe terminal output

**Expected Result**:
- ✓ Terminal shows login event information
- ✓ Output format matches:
  ```
  ====== LOGIN EVENT ======
  Time      : YYYY-MM-DD HH:MM:SS.ffffff
  Username  : [username]
  Password  : [password]
  Status    : [SUCCESS/FAILED]
  =========================
  ```

---

## Valid Test Credentials

From users.txt:
```
po → po
asd → asd
asdf → asdf
qwdf → qwef
sesha → sesha
asd → asdfg
```

Note: `asd` has two different passwords! This tests duplicate usernames.

---

## Summary of What's Being Tested

✅ Backend receives login form data
✅ Events are logged to file (login_events.txt)
✅ Successful logins are recorded
✅ Failed login attempts are recorded
✅ Timestamps are accurate
✅ Credential validation works
✅ Error messages display correctly
✅ Log file persists across sessions
✅ Data integrity in logs
✅ Terminal output verification

---

**All scenarios passing? Your application is working correctly!** ✓
